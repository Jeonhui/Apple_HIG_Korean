import os
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from Code.Convert.CustomMarkDownConverter import CustomMarkDowConverter as cmdConverter

from Code.Configure.CreationConfigure import CreationConfigure


class MarkdownConvertManager:
    config = CreationConfigure()

    def __init__(self):
        with open(self.config.url_list_file_path, 'r+') as url_list_file:
            url_list = url_list_file.readlines()

        for line in url_list[10:11]:
            data = tuple(filter(lambda x: len(x.strip()) > 0, line.split(self.config.url_list_seperator)))
            if len(data) != 3:
                continue
            keyword, url, path = data
            path = '/'.join([self.config.to_main_path, path])

            dir_path = self.__dir_path(path)
            os.makedirs(dir_path, exist_ok=True)

            driver = webdriver.Chrome()
            driver.get(url)
            WebDriverWait(driver, 1000) \
                .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#main")))
            html = driver.page_source
            soup = BeautifulSoup(html, "html5lib")
            text = cmdConverter().process_tag(soup.find('main'), convert_as_inline=False, children_only=True)
            with open(path, 'w') as f:
                f.write(text)

    def __dir_path(self, path):
        path_components = path.split('/')
        if re.match(r'^\.?[a-zA-z0-9\-]+\.[a-zA-z0-9\-]+$', path_components[-1]):
            return '/'.join(path_components[:-1])
        return path


MarkdownConvertManager()
