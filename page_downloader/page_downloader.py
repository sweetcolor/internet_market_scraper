import requests
import time

from page_downloader.browsers.browser import Browser
from page_downloader.page_checker import PageChecker


# TODO or maybe rename to page_getter cause we just get page, but not save here
class PageDownloader:
    def __init__(self, browser: Browser, page_checker: PageChecker):
        self.__browser = browser
        self.__page_checker = page_checker
        self.__session = requests.session()

    def download_page(self, link: str):
        # TODO check not valid link (here or inside Link class)
        page_source = self.__session.get(link, headers=self.__browser.get_headers()).text
        page_valid = self.__page_checker.page_is_valid(page_source)
        while not page_valid:
            time.sleep(3)
            page_source = self.__session.get(link, headers=self.__browser.get_headers()).text
            page_valid = self.__page_checker.page_is_valid(page_source)
        return page_source
