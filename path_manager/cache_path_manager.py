from path_manager.files.output_file import OutputFile
from path_manager.path_manager import PathManager
from path_manager.page.root_page import RootPage


class CachePathManager(PathManager):
    def __init__(self, page: RootPage, output_file: OutputFile):
        super().__init__(page, output_file)

    def _root_dir(self) -> str:
        return self._config.CACHE_DIRECTORY
