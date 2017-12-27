import os
from path_manager.path_manager import PathManager
from parser import Parser
from pagegetter import PageGetter


class Scraper:
    def __init__(self, start_link):
        self.start_link = start_link
        self.page_getter = PageGetter()
        self.links = []
        self.product_tabs = ['all', 'characteristics', 'review', 'photo', 'comments']
        self.curr_path_manager = None

    def crawl(self):
        self._crawl_by_categories([self.start_link])
        # self.curr_path_manager = PathManager(self.start_link, category=True)
        # self._caching_page()
        # links = Parser(self._read_cached_page()).scrap_top_category_links()
        # for link in links:
        #     self.scrap_product(link)

    def _crawl_by_categories(self, links, parent_dir=''):
        for link in links:
            self.curr_path_manager = PathManager(link, parent_dir=parent_dir)
            self._caching_page()
            new_links = Parser(self._read_cached_page()).parse_page()
            self._crawl_by_categories(new_links['categories'], self.curr_path_manager.category_dir)
            for product in new_links['products']:
                self.scrap_product(product, self.curr_path_manager.category_dir)

    def scrap_product(self, link, category_dir):
        for tab in self.product_tabs:
            tab_link = '{link}{tab}/'.format(link=link, tab=tab)
            self.curr_path_manager = PathManager(tab_link, parent_dir=category_dir, product_tab=tab)
            self._caching_page()
            result = Parser(self._read_cached_page()).scrap_product()
            self._save_res_file(result['all'])
            self._save_csv_file(result['characteristics'])

    def _caching_page(self):
        if not self._is_page_cached():
            page_source = self.page_getter.get_remote_page(self.curr_path_manager.get_link())
            self._save_page(page_source)

    def _is_page_cached(self):
        cached_page_path = self.curr_path_manager.get_cached_path()
        return os.path.isfile(cached_page_path) and os.stat(cached_page_path).st_size

    def _read_cached_page(self):
        return open(self.curr_path_manager.get_cached_path(), 'r').read()

    def _save_page(self, page_source):
        with open(self.curr_path_manager.get_cached_path(), 'w') as page:
            page.write(page_source)

    def _save_csv_file(self, result):
        self._save_res_file('\n'.join([','.join(row) for row in result]), 'csv')

    def _save_res_file(self, res, type_='html'):
        if res:
            with open(self.curr_path_manager.get_result_path(type_), 'w') as result_file:
                result_file.write(res)

    def scrap_characteristics_tab(self):
        pass


if __name__ == '__main__':
    # links_for_parsing = [
    #     # 'https://hard.rozetka.com.ua/kingston_hx421c14fb2_8/p8376719/#tab=characteristics',
    #     # 'https://bt.rozetka.com.ua/ferroli-domina-n-f24/p346495/#tab=characteristics',
    #     'https://hard.rozetka.com.ua/intel_core_i3_7100/p13244917/#tab=characteristics'
    # ]
    scraper = Scraper('https://hard.rozetka.com.ua/')
    # scraper = Scraper(links_for_parsing)
    scraper.crawl()
