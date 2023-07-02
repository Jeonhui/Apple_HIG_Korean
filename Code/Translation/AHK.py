from PapagoAPI import PapagoAPI, PapagoAPIError
from Code.Configure.TranslationConfigure import TranslationConfigure
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
            result = self.translate_markdown_file(path, start_line)

            if result is None:
                pass
            else:
                pass

            if idx == 0:
                start_line = None

    def translate_markdown_file(self, path, line=None):
        origin_file_path, translated_file_path = self.to_translated_file_path(path)
        if not os.path.isfile(origin_file_path) or not os.path.isfile(translated_file_path):
            return None

        if line is None:
            line = 0

        with open(origin_file_path) as origin_file:
            text_lines = origin_file.readlines()[line + 1:]
        current_file = open(translated_file_path, 'a')

        for line, text_line in enumerate(text_lines):
            # self.papagoAPI.translate()
            self.convert_text(text_line)
        return line

    def convert_text(self, text):
        if len(text) < 5 or text.strip()[0] in ['!', '[', '|']:
            return text, None

        converted_text = text.replace('#', '').replace('*', '')

        for repl in re.findall('\[(.*?)\]\((.*?)\)', converted_text):
            print(f"xxx [{repl[0]}]({repl[1]})")
            if repl[1][0] == '/':
                text = re.sub(repl[1], self.configure.url + repl[1], text)
            converted_text = re.sub("[" + repl[0] + "](" + repl[1] + ")", repl[0], converted_text)
        print(converted_text)
        # text.replace("[" + repl[0] + "](" + repl[1] + ")", repl[0])

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
                                       filter(lambda x: len(x.strip()) > 0,
                                              last_log.split(self.configure.log_split_keyword))))
        if len(last_log_values) < 4:
            return None, None
        path, line = last_log_values[1], int(last_log_values[2])
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
            log = list(map(lambda x: x.strip(), filter(lambda x: len(x.strip()) > 0,
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

    def write_log(self, path, line, capacity, date=datetime.now().date()):
        with open(self.configure.logs_file_path, 'a') as logs_file:
            content_list = list(map(lambda x: str(x).strip(), [date, path, line, capacity]))
            line = self.configure.log_split_keyword.join([''] + content_list + ['']) + '\n'
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

# # open origin File and current File
# originFile = open(originFilePath, 'r')
# originData = originFile.readlines()
# currentPathFile = open(currentFilePath, 'a')
#
# # empty file
# if len(originData) < 2:
#     break
#
# # read Origin Text Data
# for i in range(len(originData)):
#     # if find last log file line
#     if findLastLogFileLine:
#         if originData[i][0] != '|' and originData[i].strip() != '' and originData[i][0] != '!' and i != 0:
#
#             # remove Sharp and Asterisk
#             originText = originData[i].strip()
#             text = originText.replace('#', '').replace('*', '')
#
#             # check link and replace text
#             for repl in re.findall('\[(.*?)\]\((.*?)\)', text):
#                 originText = originText.replace(repl[1], repl[1].replace(
#                     "https://developer.apple.com/design/human-interface-guidelines", ".."))
#                 text = text.replace("[" + repl[0] + "](" + repl[1] + ")", repl[0])
#
#             # translate
#             if len(text.split(' ')) > 5:
#                 if capacity + len(originData[i]) > MAX_CAPACITY:
#                     finished = True
#                     break
#                 translatedText = translateWithPapagoAPI(text)
#
#                 if translatedText == 'error' or translatedText == '':
#                     finished = True
#                     break
#
#                 capacity += len(originData[i])
#                 currentPathFile.write(originText + '\n')
#
#                 currentPathFile.write(
#                     (('> ' + translatedText + '\n>\n\n') if translatedText[0] != '-' else (
#                             '- > ' + translatedText[1:])) + '\n\n')
#
#             else:
#                 currentPathFile.write(originText + '\n')
#
#         elif i == 0:
#             currentPathFile.write('\n')  # title
#
#         else:
#             currentPathFile.write(originData[i].strip() + '\n')  # image or table or empty