import bs4


class PageChecker:
    def __init__(self):
        pass

    # TODO save robot answer and create this method
    def page_is_valid(self, page_source: str) -> bool:
        bs_page = bs4.BeautifulSoup(page_source, 'html5lib')
        return True
