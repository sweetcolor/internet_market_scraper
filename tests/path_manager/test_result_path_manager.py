import unittest
import os

from path_manager.result_path_manager import ResultPathManager
from path_manager.files.html_file import HtmlFile
from path_manager.page.product_page import ProductPage
from path_manager.page.root_page import RootPage
from path_manager.product_tab.tab_with_single_result import TabWithSingleResult
from path_manager.product_tab.tab_with_multi_result import TabWithMultiResult
from config import RESULT_DIRECTORY


class ResultPathManagerTestCase(unittest.TestCase):
    def setUp(self):
        root_page = RootPage('https://hard.rozetka.com.ua/processors/c80083/')
        product_tab1 = TabWithSingleResult('characteristics')
        product_tab2 = TabWithMultiResult('photos')
        html_file = HtmlFile()
        page1 = ProductPage('https://hard.rozetka.com.ua/intel_core_i3_7100/p13244917',
                            root_page, product_tab1)
        self.cache_path_manager1 = ResultPathManager(page1, html_file)
        page2 = ProductPage('https://hard.rozetka.com.ua/intel_core_i3_7100/p13244917',
                            root_page, product_tab2)
        self.cache_path_manager2 = ResultPathManager(page2, html_file)

    def test_get_dir_path(self):
        self.assertEqual(self.cache_path_manager1.get_dir_path(),
                         os.path.join(RESULT_DIRECTORY, 'processors-c80083', 'intel_core_i3_7100-p13244917') +
                         os.path.sep)
        self.assertEqual(self.cache_path_manager2.get_dir_path(),
                         os.path.join(RESULT_DIRECTORY, 'processors-c80083', 'intel_core_i3_7100-p13244917', 'photos'))

    def test_get_file_path(self):
        self.assertEqual(self.cache_path_manager1.get_file_path(),
                         os.path.join(RESULT_DIRECTORY, 'processors-c80083', 'intel_core_i3_7100-p13244917',
                                      'intel_core_i3_7100-p13244917-characteristics.html'))
        self.assertEqual(self.cache_path_manager2.get_file_path(),
                         os.path.join(RESULT_DIRECTORY, 'processors-c80083', 'intel_core_i3_7100-p13244917',
                                      'photos', 'intel_core_i3_7100-p13244917-photos.html'))
