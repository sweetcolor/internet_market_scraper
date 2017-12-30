import unittest

from path_manager.page.product_page import ProductPage
from path_manager.page.root_page import RootPage
from path_manager.product_tab.tab_with_single_result import TabWithSingleResult
from path_manager.product_tab.tab_with_multi_result import TabWithMultiResult


class ProductPageTestCase(unittest.TestCase):
    def setUp(self):
        root_page = RootPage('https://hard.rozetka.com.ua/processors/c80083/')
        product_tab1 = TabWithSingleResult('characteristics')
        product_tab2 = TabWithMultiResult('photos')
        self.product_page1 = ProductPage('https://hard.rozetka.com.ua/intel_core_i3_7100/p13244917',
                                         root_page, product_tab1)
        self.product_page2 = ProductPage('https://hard.rozetka.com.ua/intel_core_i3_7100/p13244917',
                                         root_page, product_tab2)

    def test_get_tab_sub_dir(self):
        self.assertEqual(self.product_page1.get_tab_sub_dir(), '')
        self.assertEqual(self.product_page2.get_tab_sub_dir(), 'photos')

    def test_get_tab_name(self):
        self.assertEqual(self.product_page1.get_tab_name(), 'characteristics')
        self.assertEqual(self.product_page2.get_tab_name(), 'photos')
