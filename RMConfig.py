from enum import Enum
import json

class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class RMConfigKey(StrEnum):
    sidebar_path = 'sidebar_path'
    depth_keyword = 'depth_keyword'

    readme_file_name = 'readme_file_name'
    start_path = 'start_path'
    readme_base = 'readme_base'

    url_list_file_name = 'url_list_file_name'
    start_url = 'start_url'
    url_list_base = 'url_list_base'

    line_seperator = 'line_seperator'
    url_list_seperator = 'url_list_seperator'

class RMConfig:
    def __init__(self):
        with open('configure.json','r') as c:
            configure = json.load(c)
            self.sidebar_path = configure[RMConfigKey.sidebar_path.value]
            self.depth_keyword = configure[RMConfigKey.depth_keyword.value]
            self.readme_file_name = configure[RMConfigKey.readme_file_name.value]
            self.start_path = configure[RMConfigKey.start_path.value]
            self.readme_base = configure[RMConfigKey.readme_base.value]
            self.url_list_file_name = configure[RMConfigKey.url_list_file_name.value]
            self.start_url = configure[RMConfigKey.start_url.value]
            self.url_list_base = configure[RMConfigKey.url_list_base.value]
            self.line_seperator = configure[RMConfigKey.line_seperator.value]
            self.url_list_seperator = configure[RMConfigKey.url_list_seperator.value]