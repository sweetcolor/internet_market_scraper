from path_manager.page.page import Page
from path_manager.page.root_page import RootPage
from path_manager.product_tab.product_tab import ProductTab


class ProductPage(Page):
    def __init__(self, link: str, parent_page: RootPage, product_tab: ProductTab):
        super().__init__(link, parent_page)
        self.product_tab = product_tab

    def get_tab_sub_dir(self) -> str:
        return self.product_tab.get_sub_dir()

    def get_tab_name(self):
        return self.product_tab.name
