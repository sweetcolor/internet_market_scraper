import requests

from downloader.browsers.browser import Browser


# TODO or maybe rename to page_getter cause we just get page, but not save here
class LinkDownloader:
    def __init__(self, browser: Browser):
        self.__browser = browser
        self.__session = requests.session()

    def download(self, link: str) -> requests.Response:
        # TODO check not valid link (here or inside Link class)
        return self.__session.get(link, headers=self.__browser.get_headers())
