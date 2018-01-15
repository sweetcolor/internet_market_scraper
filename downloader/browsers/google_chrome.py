from downloader.browsers.browser import Browser


class GoogleChrome(Browser):
    def _get_user_agent(self):
        return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 ' \
               'Safari/537.36 '
