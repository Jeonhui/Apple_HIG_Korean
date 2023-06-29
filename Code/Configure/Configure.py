from enum import Enum
import json

class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class ConfigureKey(StrEnum):
    chromedriver_path = 'chromedriver_path'
    to_main_path = 'to_main_path'

    sidebar_path = 'sidebar_path'
    depth_keyword = 'depth_keyword'

    readme_file_name = 'readme_file_name'
    translated_markdown_path = 'translated_markdown_path'
    origin_markdown_path = 'origin_markdown_path'
    readme_base = 'readme_base'

    url_list_file_path = 'url_list_file_path'
    start_url = 'start_url'
    url_list_base = 'url_list_base'

    line_seperator = 'line_seperator'
    url_list_seperator = 'url_list_seperator'

    change_keyword_key = 'change_keyword_key'
    change_keyword2_key = 'change_keyword2_key'
    change_path_key = 'change_path_key'
    main_title = 'main_title'
    sub_title = 'sub_title'
    sub_title2 = 'sub_title2'
    line_seperator2 = 'line_seperator2'

    base_file_join_key = 'base_file_join_key'
    base_file_title = 'base_file_title'
    base_file_subtitle = 'base_file_subtitle'

    link = 'link'


class Configure:
    def __init__(self):
        with open('../Configure/configure.json', 'r') as c:
            configure = json.load(c)
            self.chromedriver_path = configure[ConfigureKey.chromedriver_path.value]
            self.to_main_path = configure[ConfigureKey.to_main_path.value]
            self.sidebar_path = configure[ConfigureKey.sidebar_path.value]
            self.depth_keyword = configure[ConfigureKey.depth_keyword.value]
            self.readme_file_name= configure[ConfigureKey.readme_file_name.value]
            self.translated_markdown_path = configure[ConfigureKey.translated_markdown_path.value]
            self.origin_markdown_path = configure[ConfigureKey.origin_markdown_path.value]
            self.readme_base = configure[ConfigureKey.readme_base.value]
            self.url_list_file_path = configure[ConfigureKey.url_list_file_path.value]
            self.start_url = configure[ConfigureKey.start_url.value]
            self.url_list_base = configure[ConfigureKey.url_list_base.value]
            self.line_seperator = configure[ConfigureKey.line_seperator.value]
            self.url_list_seperator = configure[ConfigureKey.url_list_seperator.value]
            self.change_keyword_key = configure[ConfigureKey.change_keyword_key.value]
            self.change_keyword2_key = configure[ConfigureKey.change_keyword2_key.value]
            self.change_path_key = configure[ConfigureKey.change_path_key.value]
            self.main_title = configure[ConfigureKey.main_title.value]
            self.sub_title = configure[ConfigureKey.sub_title.value]
            self.sub_title2 = configure[ConfigureKey.sub_title2.value]
            self.line_seperator2 = configure[ConfigureKey.line_seperator2.value]
            self.base_file_join_key = configure[ConfigureKey.base_file_join_key.value]
            self.base_file_title = configure[ConfigureKey.base_file_title.value]
            self.base_file_subtitle = configure[ConfigureKey.base_file_subtitle.value]
            self.link = configure[ConfigureKey.link.value]
