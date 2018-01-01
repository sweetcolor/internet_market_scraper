import requests
import os
import time


class PageGetter:
    def __init__(self, browser='firefox'):
        self.browser = browser
        # self.driver = webdriver.PhantomJS()
        self.tmp_page_name = '.raw_tmp.html'
        self.headers = self._headers_list()
        self.session = requests.session()
    #
    # def prepare_driver(self):
    #     webdriver.DesiredCapabilities.PHANTOMJS["browserName"] = webdriver.DesiredCapabilities.FIREFOX["browserName"]
    #     for key, value in self.headers[browser].items():
    #         # capability_key = 'phantomjs.page.customHeaders.{}'.format(key)
    #         webdriver.DesiredCapabilities.PHANTOMJS[key] = value
    #     return webdriver.PhantomJS()

    def get_remote_page(self, link):
        return self._execute_page(self.session.get(link, headers=self.headers).text)

    def _execute_page(self, raw_page):
        self._save_tmp_raw_page(raw_page)
        time.sleep(3)
        # self.driver.get('file://{}'.format(os.path.join(os.getcwd(), self.tmp_page_name)))
        # page_source = self.driver.page_source
        self._remove_tmp_raw_page()
        return page_source

    def _save_tmp_raw_page(self, raw_page):
        with open(self.tmp_page_name, 'w') as tmp_file:
            tmp_file.write(raw_page)

    def _remove_tmp_raw_page(self):
        os.remove(self.tmp_page_name)

    def _headers_list(self):
        common_params = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        browser_params = {
            'firefox': {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
            },
            'chrome': {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/62.0.3202.89 Safari/537.36 '
            }
        }
        return dict(common_params, **browser_params[self.browser])
