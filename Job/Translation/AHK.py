from Job.Translation.PapagoAPI import PapagoAPI
from Job.Configure.TranslationConfigure import TranslationConfigure
from Job.Translation.AHKError import AHKError
from datetime import datetime
import re
import os


class AHKModel:
    papagoAPI = PapagoAPI()
    configure = TranslationConfigure()

    def start(self):
        self.papagoAPI.set_capacity(self.get_today_capacity())
        start_path, start_line = self.find_last_log()
        path_list = self.find_path_list(start_path)
        for idx, path in enumerate(path_list):
            line, error_code = self.translate_markdown_file(path, start_line)
            if error_code == AHKError.OverCapacityError.value:
                self.write_log(path, line,
                               capacity=self.papagoAPI.capacity)
                break

            self.write_log(path, line,
                           capacity=self.papagoAPI.capacity,
                           error_code=error_code)
            if error_code is not None:
                break

            if idx == 0:
                start_line = None

    def translate_markdown_file(self, path, line=None):
        origin_file_path, translated_file_path = self.to_translated_file_path(path)
        if not os.path.isfile(origin_file_path) or not os.path.isfile(translated_file_path):
            print(f">>>>>>>>>>>>>>>>>>> {origin_file_path}, {translated_file_path}")
            return line, AHKError.FileNotFoundError.value

        if line is None:
            line = 0

        with open(origin_file_path) as origin_file:
            text_lines = origin_file.readlines()[line + 1:]
        translated_file = open(translated_file_path, 'a')

        for line, text_line in enumerate(text_lines):
            text, converted_text = self.convert_text(line, text_line)
            translated_file.write(f"{text}\n")
            if converted_text is not None:
                translated_text = self.papagoAPI.translate(text)
                if translated_text is AHKError.ResponseError:
                    return line, translated_text.value
                if translated_text is AHKError.OverCapacityError:
                    return line, translated_text.value

                translated_text = f"> {translated_text}\n>\n\n" \
                    if translated_text[0] != '-' \
                    else f"- > {translated_text}\n\n"
                translated_file.write(translated_text)
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

    def get_today_capacity(self):
        total_capacity = sum(list(map(lambda x: int(x[3]),
                                      self.read_log(datetime.now().date()))))
        return total_capacity

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

    def write_log(self, path, line, capacity, error_code=None, date=datetime.now().date()):
        date = date.strftime(self.configure.datetime_format)
        with open(self.configure.logs_file_path, 'a') as logs_file:
            content_list = list(map(lambda x: str(x).strip(), [date, path, line, capacity]))
            line = self.configure.log_split_keyword.join([''] +
                                                         content_list +
                                                         [str(error_code) if error_code is not None else ''] +
                                                         ['']) + '\n'
            logs_file.write(line)

    def to_translated_file_path(self, path, to_main_path=True):
        origin_file_path = re.sub(self.configure.translated_markdown, self.configure.origin_markdown, path)
        translated_file_path = re.sub(self.configure.origin_markdown, self.configure.translated_markdown, path)
        return (self.to_main_path(origin_file_path), self.to_main_path(translated_file_path)) \
            if to_main_path \
            else (origin_file_path, translated_file_path)

    def to_main_path(self, path):
        return f"{self.configure.to_main_path}/{path}"


AHKModel().start()
