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
        return full_path

    # TODO move to another class
    def create_directory(self) -> None:
        full_path = self.get_dir_path()
        if not os.path.exists(full_path):
            os.mkdir(full_path)

    # TODO move to another class
    def remove_directory(self) -> None:
        full_path = self.get_dir_path()
        if not os.path.exists(full_path):
            os.rmdir(full_path)

    def _file_name(self) -> str:
        name = self.page.get_link_name()
        tab_prefix = '-{}'.format(self.page.get_tab_name()) if self.page.get_tab_name() else ''
        extension = self.output_file.ext
        return f'{name}{tab_prefix}.{extension}'

    @abc.abstractmethod
    def _root_dir(self) -> str:
        pass
