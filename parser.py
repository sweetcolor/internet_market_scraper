import re
from bs4 import BeautifulSoup
from bs4 import Tag
from bs4 import NavigableString


class Parser:
    def __init__(self, page):
        self.bs_page = BeautifulSoup(page, 'html5lib')
        self.goods = self.bs_page.find('div', {'id': 'catalog_goods_block'})
        self.category_block = self.bs_page.find('div', {'class': 'pab-table'})
        self.details_character = self.bs_page.find('div', {'class': 'detail-tabs'})
        self.details_all = self.bs_page.find('div', {'class': 'detail-col-description'})
        self.comments = self.bs_page.find('div', {'id': 'comments'})
        self.product_tabs = {
            'all': self.scrap_all_tab,
            'characteristics': self.scrap_characteristics_tab,
            'review': self.scrap_review_tab,
            'photo': self.scrap_photo_tab,
            'comments': self.scrap_comments_tab
        }

    def scrap_product(self):
        result = {
            'all': '',
            'characteristics': list(),
            'review': list(),
            'photo': list(),
            'comments': dict()
        }
        active_a = self.details_character.find('ul', {'id': 'tabs'}).find('a', {'class': 'novisited m-tabs-link active'})
        tab_name = active_a.parent.attrs['name']
        result[tab_name] = self.product_tabs[tab_name]()
        return result

    def scrap_all_tab(self):
        desc = self.details_all.find('section', {'class': 'detail-tabs-i'})
        res = []
        for child in desc.children:
            if isinstance(child, NavigableString):
                continue
            if isinstance(child, Tag):
                if child.text and child.name != 'a':
                    res.append(child)
        return '\n'.join([str(tag) for tag in res])

    def scrap_characteristics_tab(self):
        title = self.bs_page.find(re.compile('h[1-6]'), {'class': 'detail-title'}).get_text()
        title = self._full_str_strip(title)
        result = [['Назва', title]]
        tab_content = self.details_character.find('div', {'id': 'tab_content'})
        prod_char_table = tab_content.table
        prod_char_tr = prod_char_table.find_all('tr')
        for tr in prod_char_tr:
            row = [self._full_str_strip(str(td.text)) for td in tr.find_all('td')]
            result.append(row)
        return result

    def scrap_review_tab(self):
        pass

    def scrap_photo_tab(self):
        pass

    def scrap_comments_tab(self):
        comments = self.comments.find_all('article', {'class': 'pp-review-i'})
        res = []
        for comment in comments:
            res.append({})
            res['date'] = comment.find('time', {'class': 'pp-review-date-text'}).get_text()
            res['author'] = comment.find('span', {'class': 'pp-review-author-name'}).get_text()
            res['review'] = [
                review.get_text() for review in comment.find_next_siblings('div', {'class': 'pp-review-text-i'})
            ]
            res['answer'] = [comment.find_all('div', {'class': 'pp-comments-answer'})]

    def scrap_product_list(self):
        a_tags = self.goods.find_all('a', {'class': 'responsive-img centering-child-img'})
        product_links = [item.attrs['href'] for item in a_tags]
        return product_links

    def scrap_top_category_links(self):
        category_links = [a.attrs['href'] for a in self.category_block.find_all('a', {'class': 'pab-h3-link'})]
        return category_links

    def parse_page(self):
        result = dict(products=list(), categories=list())
        if self.goods:
            result['products'] = self.scrap_product_list()
        if self.category_block:
            result['categories'] = self.scrap_top_category_links()
        return result

    @staticmethod
    def _full_str_strip(str_):
        f = re.findall('[a-zA-Z0-9а-яА-ЯЇІЄҐїієґ /()]', str_.strip())
        return ''.join(f)
