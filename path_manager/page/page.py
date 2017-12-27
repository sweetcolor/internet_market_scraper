from path_manager.page.root_page import RootPage


class Page(RootPage):
    def __init__(self, link: str, parent_page: RootPage):
        super().__init__(link)
        self.parent_page = parent_page

    def get_parent_page_link_name(self) -> str:
        return self.parent_page.get_link_name()
