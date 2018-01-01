from page_downloader.browsers.browser import Browser


class Firefox(Browser):
    def _get_user_agent(self):
        return 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'
