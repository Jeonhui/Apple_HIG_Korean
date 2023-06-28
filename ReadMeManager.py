import re


class ReadMeManager:
    title = """# **[Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/guidelines/overview/) 번역**  
![https://img.shields.io/badge/papago-blue?style=for-the-badge&](https://img.shields.io/badge/papago-blue?style=for-the-badge&)
![https://img.shields.io/badge/githubAction-lightgray?style=for-the-badge&](https://img.shields.io/badge/githubActionS-lightgray?style=for-the-badge&)
"""
    depth_keyword = '- '
    start_path = '.'

    def __init__(self):
        with open('sidebar.md', 'r') as f:
            self.sidebar_text_list = f.readlines()

    def create_readme(self):
        path_list = [self.start_path]
        prev_depth = 0
        for text_line in self.sidebar_text_list:
            depth = len(re.findall(self.depth_keyword, text_line))
            text_line = re.sub('- ', ' ', text_line).strip()

            if depth == 0:
                path_list = [self.start_path]
            elif prev_depth > depth:
                path_list = path_list[:len(path_list) - (prev_depth - depth + 1)]
            elif prev_depth == depth:
                path_list = path_list[:-1]
            path_list = path_list + [text_line]

            if path_list[-1] != '':
                path = '/'.join(path_list) + '.md'


            prev_depth = depth

    def create_local_path_list(self):
        1


readmeManager = ReadMeManager()
readmeManager.create_readme()
readmeManager.create_path_list()
