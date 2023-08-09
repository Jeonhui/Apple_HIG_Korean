from enum import Enum
import json


class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class TranslationConfigureKey(StrEnum):
    url_list_file_path = 'url_list_file_path'
    logs_file_path = 'logs_file_path'
    url_list_split_keyword = 'url_list_split_keyword'
    log_split_keyword = 'log_split_keyword'
    datetime_format = 'datetime_format'
    origin_markdown = 'origin-markdown'
    translated_markdown = 'translated-markdown'
    to_main_path = 'to_main_path'
    url = 'url'
    prev_path = 'prev_path'
    main_path_to = 'main_path_to'

class TranslationConfigure:
    def __init__(self, test=False):
        if test:
            with open('../Configure/testingTranslationConfigure.json', 'r') as c:
                configure = json.load(c)
        else:
            with open('Job/Configure/translationConfigure.json', 'r') as c:
                configure = json.load(c)

        self.url_list_file_path = configure[TranslationConfigureKey.url_list_file_path.value]
        self.logs_file_path = configure[TranslationConfigureKey.logs_file_path.value]
        self.url_list_split_keyword = configure[TranslationConfigureKey.url_list_split_keyword.value]
        self.log_split_keyword = configure[TranslationConfigureKey.log_split_keyword.value]
        self.datetime_format = configure[TranslationConfigureKey.datetime_format.value]
        self.origin_markdown = configure[TranslationConfigureKey.origin_markdown.value]
        self.translated_markdown = configure[TranslationConfigureKey.translated_markdown.value]
        self.to_main_path = configure[TranslationConfigureKey.to_main_path.value]
        self.url = configure[TranslationConfigureKey.url.value]
        self.prev_path = configure[TranslationConfigureKey.prev_path.value]
        self.main_path_to = configure[TranslationConfigureKey.main_path_to.value]
