from Job.Translation.PapagoAPI import PapagoAPI
from Job.Configure.TranslationConfigure import TranslationConfigure
from Job.Translation.AHKError import AHKError
from datetime import datetime
import re
import os


class AHKModel:
    papagoAPI = PapagoAPI()
    configure = None
    testCnt = 0
    testMaxCnt = 10000

    def __init__(self):
        pass

    def start(self, test=False):
        # test일 경우 test configuration 사용
        if test:
            self.configure = TranslationConfigure(test=True)
        else:
            self.configure = TranslationConfigure()
        # papago API 사용량 확인 및 설정
        self.papagoAPI.set_capacity(self.get_today_capacity())

        # 시작 경로와 번역 마무리 줄 수 확인
        start_path, start_line = self.find_last_log()
        path_list = self.find_path_list(start_path)

        # 경로 목록을 가지고 번역을 실행
        for path in path_list:
            line, error_code = self.translate_markdown_file(path, start_line, test)
            # error code 확인
            if test:
                print(f"(test) error_code: {error_code}, capacity: {self.testCnt}")
            else:
                print(f"error_code: {error_code}, capacity: {self.papagoAPI.capacity}")
            if error_code == AHKError.OverCapacityError.value:
                self.write_log(path, line,
                               capacity=self.papagoAPI.capacity)
                return

            # log 작성
            self.write_log(path, line,
                           capacity=self.papagoAPI.capacity,
                           error_code=error_code)

            if error_code is not None:
                return

    # Markdown 번역
    def translate_markdown_file(self, path, line=None, test=False):
        # 해당 경로 파일 확인
        origin_file_path, translated_file_path = self.to_translated_file_path(path)
        if not os.path.isfile(origin_file_path) or not os.path.isfile(translated_file_path):
            print(f"Error: FileNotFoundError {origin_file_path}, {translated_file_path}")
            return line, AHKError.FileNotFoundError.value

        # line이 None으로 지정되면 0번째부터 시작
        if line is None or line == 'None':
            line = 0

        # 해당 MarkDown 원본 파일 읽기 (선택한 다음 줄부터)
        with open(origin_file_path) as origin_file:
            text_lines = origin_file.readlines()
        translated_file = open(translated_file_path, 'a')

        for text_line in text_lines[line + 1:]:
            text, converted_text = self.convert_text(line, text_line)
            translated_file.write(f"{text}\n")
            if converted_text is not None:
                if test:
                    self.testCnt += len(converted_text)
                    translated_text = converted_text
                    if self.testCnt > self.testMaxCnt:
                        translated_text = AHKError.OverCapacityError
                        return line, translated_text.value
                else:
                    translated_text = self.papagoAPI.translate(text)
                if translated_text is AHKError.ResponseError:
                    return line, translated_text.value
                if translated_text is AHKError.OverCapacityError:
                    return line, translated_text.value

                translated_text = f"> {translated_text}\n>\n\n" \
                    if translated_text[0] != '-' \
                    else f"- > {translated_text}\n\n"
                translated_file.write(translated_text)
            line += 1
        return line, None

    def convert_text(self, line, text):
        if line == 0 or len(text.strip().split(' ')) < 5:
            return text, None
        if len(text) < 5 or text.strip()[0] in ['!', '[', '|']:
            return text, None

        converted_text = text.strip().replace('#', '').replace('*', '')

        for repl in re.findall('\[(.*?)]\((.*?\)*)\)', converted_text):
            if len(repl[1]) > 0 and repl[1][0] == '/':
                text = re.sub(repl[1], self.configure.url + repl[1], text)
            changed_repl_0 = repl[0].replace('-', '\-')
            changed_repl_1 = repl[1].replace('-', '\-')
            converted_text = re.sub(f"\[{changed_repl_0}]\({changed_repl_1}\)", repl[0], converted_text)
        return text, converted_text

    def find_path_list(self, start_path=None):
        with open(self.configure.url_list_file_path) as url_list_file:
            path_list = url_list_file.readlines()[2:]
            path_list = list(map(lambda x: list(filter(lambda y: len(y.strip()) > 0,
                                                       x.split(self.configure.log_split_keyword)))[2].strip(),
                                 path_list))

        if start_path is None:
            return path_list

        start_path = re.sub(self.configure.translated_markdown, self.configure.origin_markdown, start_path)
        for idx, path in enumerate(path_list):
            path = re.sub(self.configure.translated_markdown, self.configure.origin_markdown, path)
            if start_path == path:
                return path_list[idx:]
        return path_list

    def find_last_log(self):
        with open(self.configure.logs_file_path, 'r') as logs_file:
            last_log = logs_file.readlines()[-1]
            last_log_values = list(map(lambda x: x.strip(),
                                       filter(lambda x: (len(x.strip()) > 0 and x.strip()[0] != '-'),
                                              last_log.split(self.configure.log_split_keyword))))
        if len(last_log_values) < 5:
            return None, None
        path, line = last_log_values[1], max(0, int(last_log_values[2]) - (1 if last_log_values[4] == '' else 0))
        return path, line

    # Papago API 하루 사용량 확인
    def get_today_capacity(self):
        total_capacity = sum(list(map(lambda x: int(x[3]),
                                      self.read_log(datetime.now().date()))))
        return total_capacity

    # read log
    def read_log(self, date=None):
        with open(self.configure.logs_file_path, 'r') as logs_file:
            logs_lines = logs_file.readlines()[2:]
        date_log = []
        for log in logs_lines:
            log = list(map(lambda x: x.strip(), filter(lambda x: (len(x.strip()) > 0 and x.strip()[0] != '-'),
                                                       log.split(self.configure.log_split_keyword))))
            if len(log) < 4:
                continue
            log_date = datetime.strptime(log[0], self.configure.datetime_format).date()
            if date is not None:
                if log_date == date:
                    date_log.append(log)
            else:
                date_log.append(log)
        return date_log

    # log 기록
    def write_log(self, path, line, capacity, error_code=None, date=datetime.now().date()):
        date = date.strftime(self.configure.datetime_format)
        with open(self.configure.logs_file_path, 'a') as logs_file:
            content_list = list(map(lambda x: str(x).strip(), [date, path, line, capacity]))
            line = self.configure.log_split_keyword.join([''] +
                                                         content_list +
                                                         [str(error_code) if error_code is not None else '.'] +
                                                         ['']) + '\n'
            logs_file.write(line)

    # translated_file path 변환
    def to_translated_file_path(self, path, to_main_path=False):
        origin_file_path = re.sub(self.configure.translated_markdown, self.configure.origin_markdown, path)
        translated_file_path = re.sub(self.configure.origin_markdown, self.configure.translated_markdown, path)
        return (self.to_main_path(origin_file_path), self.to_main_path(translated_file_path)) \
            if to_main_path \
            else (origin_file_path, translated_file_path)

    # main path로 path 변환
    def to_main_path(self, path):
        return f"{self.configure.to_main_path}/{path}"