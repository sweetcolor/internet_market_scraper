import os

from path_manager.files.output_file import OutputFile
from path_manager.page.root_page import RootPage
from path_manager.path_manager import PathManager


class ResultPathManager(PathManager):
    def __init__(self, page: RootPage, output_file: OutputFile):
        super().__init__(page, output_file)

    def get_dir_path(self):
        return os.path.join(super().get_dir_path(), self.page.get_tab_sub_dir())

    def _root_dir(self):
        return self._config.RESULT_DIRECTORY
