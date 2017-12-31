import unittest
import os

from path_manager.cache_path_manager import CachePathManager
from path_manager.files.html_file import HtmlFile
from path_manager.page.product_page import ProductPage
from path_manager.page.root_page import RootPage
from path_manager.product_tab.tab_with_single_result import TabWithSingleResult
from config import CACHE_DIRECTORY


class CachePathManagerTestCase(unittest.TestCase):
    def setUp(self):
        root_page = RootPage('https://hard.rozetka.com.ua/processors/c80083/')
        product_tab1 = TabWithSingleResult('characteristics')
        html_file = HtmlFile()
        page = ProductPage('https://hard.rozetka.com.ua/intel_core_i3_7100/p13244917',
                           root_page, product_tab1)
        self.cache_path_manager = CachePathManager(page, html_file)

    def test_get_dir_path(self):
        self.assertEqual(self.cache_path_manager.get_dir_path(),
                         os.path.join(CACHE_DIRECTORY, 'processors-c80083', 'intel_core_i3_7100-p13244917'))

    def test_get_file_path(self):
        self.assertEqual(self.cache_path_manager.get_file_path(),
                         os.path.join(CACHE_DIRECTORY, 'processors-c80083', 'intel_core_i3_7100-p13244917',
                                      'intel_core_i3_7100-p13244917-characteristics.html'))
