import urllib.parse


class RootPage:
    def __init__(self, link: str):
        self.link = link

    def get_parent_page_link_name(self) -> str:
        return ''

    def get_tab_sub_dir(self) -> str:
        return ''

    def get_tab_name(self) -> str:
        return ''

    def get_link_name(self) -> str:
        parsed_link = urllib.parse.urlparse(self.link)
        path = parsed_link.path.strip('/').replace('/', '-')
        if not path:
            return parsed_link.hostname
        return path
