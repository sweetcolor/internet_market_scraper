import abc
import os
import config

from path_manager.files.output_file import OutputFile
from path_manager.page.root_page import RootPage


class PathManager(abc.ABC):
    def __init__(self, page: RootPage, output_file: OutputFile):
        self._config = config
        self.page = page
        self.output_file = output_file

    def get_file_path(self) -> str:
        return os.path.join(self.get_dir_path(), self._file_name())

    def get_dir_path(self) -> str:
        full_path = os.path.join(self._root_dir(), self.page.get_parent_page_link_name(), self.page.get_link_name())
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        return full_path

    def _file_name(self) -> str:
        name = self.page.get_link_name()
        tab_prefix = '-{}'.format(self.page.get_tab_name()) if self.page.get_tab_name() else ''
        extension = self.output_file.ext
        return f'{name}{tab_prefix}.{extension}'

    @abc.abstractmethod
    def _root_dir(self) -> str:
        pass


# class PathManager:
#     def __init__(self, link, parent_dir='', product_tab=''):
#         self.link = link
#         self.parsed_link = urllib.parse.urlparse(self.link)
#         self.product_tab = product_tab
#         self._path = self._extract_path_from_link()
#         self.file_name = self._get_file_name()
#         self.category_dir = self._get_category_dir(parent_dir)
#         self.cashed_dir = self._get_parent_dir(config.CACHE_DIRECTORY)
#         self.result_dir = self._get_parent_dir(config.RESULT_DIRECTORY)
#
#     def get_link(self):
#         return self.link
#
#     def get_result_path(self, extension_file='csv'):
#         return self._file_path(self.result_dir, extension_file)
#
#     def get_cached_path(self, extension_file='html'):
#         return self._file_path(self.cashed_dir, extension_file)
#
#     def get_cached_dir(self):
#         return self.cashed_dir
#
#     def get_result_dir(self):
#         return self.result_dir
#
#     def _extract_path_from_link(self):
#         path = self.parsed_link.path.strip('/').replace('/', '-')
#         if self.product_tab and path.endswith(self.product_tab):
#             path = path[:len(path)-len(self.product_tab)-1]
#         if not path:
#             return self.parsed_link.hostname
#         return path
#
#     def _get_file_name(self):
#         sep = '-' if self.product_tab else ''
#         return '{name}{sep}{tab}'.format(name=self._path, sep=sep, tab=self.product_tab)
#
#     def _get_parent_dir(self, parent):
#         full_path = os.path.join(parent, self.category_dir)
#         if not os.path.exists(full_path):
#             os.mkdir(full_path)
#         return full_path
#
#     def _get_category_dir(self, parent_dir):
#         parent_dir = os.path.join(parent_dir, self._path)
#         return parent_dir
#
#     def _file_path(self, dir_name, extension):
#         return os.path.join(dir_name, '{name}.{ext}'.format(name=self.file_name, ext=extension))
