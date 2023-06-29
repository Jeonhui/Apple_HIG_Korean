import re
import json
from RMConfig import RMConfig


class ReadMeManager:
    config = RMConfig()

    def __init__(self):
        with open(self.config.sidebar_path, 'r') as f:
            self.sidebar_text_list = f.readlines()

    def create(self):
        path_components = [self.config.start_path]
        prev_depth = 0
        path_list = []
        for text_line in self.sidebar_text_list:
            depth = len(re.findall(self.config.depth_keyword, text_line))
            text_line = re.sub('- ', ' ', text_line).strip()

            if depth == 0:
                path_components = [self.config.start_path]
            elif prev_depth > depth:
                path_components = path_components[:len(path_components) - (prev_depth - depth + 1)]
            elif prev_depth == depth:
                path_components = path_components[:-1]
            path_components = path_components + [text_line]

            if path_components[-1] != '':
                path_list.append(path_components)
            prev_depth = depth
        self.create_readme(path_list)
        # self.create_url_list(path_list)

    def create_readme(self, path_list):
        for path_components in path_list:
            key, path = self.__toPath(path_components)
            print(key, path)

    def create_url_list(self, path_list):
        with open(self.config.url_list_file_name, 'w') as url_list_file:
            url_list_file.write(self.config.url_list_base)
            for path_components in path_list:
                key, url = self.__toPath(path_components, url=True)
                line = self.config.url_list_seperator.join(['', key, url, '', '']) + \
                    self.config.line_seperator
                url_list_file.write(line)

    def __toPath(self, path_components, url=False):
        key = path_components[-1]
        last_components = re.sub(' ', '-', path_components[-1].lower())
        if url:
            url = '/'.join([self.config.start_url, last_components])
            return key, url
        else:
            path = '/'.join(path_components[:-1] + [last_components]) + '.md'
            return key, path


ReadMeManager().create()
