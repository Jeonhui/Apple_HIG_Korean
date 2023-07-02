import re
import os
from Job.Configure.CreationConfigure import CreationConfigure


class ReadMeManager:
    config = CreationConfigure()

    def __init__(self):
        with open(self.config.sidebar_path, 'r') as f:
            self.sidebar_text_list = f.readlines()

    def create(self):
        path_components = [self.config.translated_markdown_path]
        prev_depth = 0
        path_list = []
        for text_line in self.sidebar_text_list:
            depth = len(re.findall(self.config.depth_keyword, text_line))
            text_line = re.sub('- ', ' ', text_line).strip()

            if depth == 0:
                path_components = [self.config.translated_markdown_path]
            elif prev_depth > depth:
                path_components = path_components[:len(path_components) - (prev_depth - depth + 1)]
            elif prev_depth == depth:
                path_components = path_components[:-1]
            path_components = path_components + [text_line]

            if path_components[-1] != '':
                path_list.append(path_components)
            prev_depth = depth
        # self.create_readme(path_list)
        self.create_url_list(path_list)
        # self.create_base_file(path_list)

    def create_readme(self, path_list):
        readme_file_path = '/'.join([self.config.to_main_path, self.config.readme_file_name])
        with open(readme_file_path, 'w') as readme_file:
            readme_file.write(self.config.readme_base)
            for path_components in path_list:
                keyword, path = self.__toPath([self.config.origin_markdown_path] + path_components[1:])
                line = self.__change_readme_line(keyword, path, depth=(len(path_components) - 2))
                readme_file.write(line)

    def create_url_list(self, path_list):
        with open(self.config.url_list_file_path, 'w') as url_list_file:
            url_list_file.write(self.config.url_list_base)
            for path_components in path_list:
                keyword, url = self.__toPath(path_components, url=True)
                _, path = self.__toPath([self.config.origin_markdown_path] + path_components[1:])
                line = self.config.url_list_seperator.join(['', keyword, url, path, '', '']) + \
                       self.config.line_seperator
                url_list_file.write(line)

    def create_base_file(self, path_list):
        for path_components in path_list:
            keyword, path = self.__toPath(path_components, with_main_path=True)
            dir_path = self.__dir_path(path)
            os.makedirs(dir_path, exist_ok=True)
            with open(path, 'w') as file:

                subtitle = ''
                subtitle_keyword = self.config.base_file_join_key.join(path_components[1:-1]).strip()
                if len(subtitle_keyword) > 0:
                    _, subtitle_path = self.__toPath(path_components[:-1])

                    link_subtitle_keyword = re.sub(self.config.change_keyword_key,
                                                   subtitle_keyword,
                                                   self.config.link)
                    link_subtitle_keyword = re.sub(self.config.change_path_key,
                                                   subtitle_path,
                                                   link_subtitle_keyword)
                    subtitle = re.sub(self.config.change_keyword_key,
                                      link_subtitle_keyword,
                                      self.config.base_file_subtitle)
                title = re.sub(self.config.change_keyword_key, keyword, self.config.base_file_title)

                line = subtitle + self.config.line_seperator + title
                file.write(line)

    def __toPath(self, path_components, url=False, with_main_path=False):
        keyword = path_components[-1]
        change = lambda x: re.sub(' ', '-', x.lower())
        path_components = list(map(change, path_components))
        last_component = path_components[-1]
        if url:
            path = '/'.join([self.config.start_url, last_component])
        elif with_main_path:
            path = '/'.join([self.config.to_main_path] + path_components[:-1] + [last_component]) + '.md'
        else:
            path = '/'.join(path_components[:-1] + [last_component]) + '.md'
        return keyword, path

    def __change_readme_line(self, keyword, path, depth):
        if depth < 1:
            line = self.config.line_seperator2 + self.config.main_title
        elif depth == 1:
            line = self.config.sub_title
        else:
            line = self.config.sub_title2
        line = re.sub(self.config.change_keyword_key, keyword, line)
        line = re.sub(self.config.change_path_key, path, line)
        return line

    def __dir_path(self, path):
        path_components = path.split('/')
        if re.match(r'^\.?[a-zA-z0-9\-]+\.[a-zA-z0-9\-]+$', path_components[-1]):
            return '/'.join(path_components[:-1])
        return path


ReadMeManager().create()
