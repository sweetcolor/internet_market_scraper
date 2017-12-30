import unittest

from path_manager.page.root_page import RootPage


class RootPageTestCase(unittest.TestCase):
    def setUp(self):
        self.page1 = RootPage('https://hard.rozetka.com.ua')
        self.page2 = RootPage('https://hard.rozetka.com.ua/intel_core_i3_7100/p13244917/')

    def test_get_link_name(self):
        self.assertEqual(self.page1.get_link_name(), 'hard.rozetka.com.ua')
        self.assertEqual(self.page2.get_link_name(), 'intel_core_i3_7100-p13244917')

    def test_get_parent_page_link_name(self):
        self.assertEqual(self.page1.get_parent_page_link_name(), '')
        self.assertEqual(self.page2.get_parent_page_link_name(), '')

    def test_get_tab_sub_dir(self):
        self.assertEqual(self.page1.get_tab_sub_dir(), '')
        self.assertEqual(self.page2.get_tab_sub_dir(), '')

    def test_get_tab_name(self):
        self.assertEqual(self.page1.get_tab_name(), '')
        self.assertEqual(self.page2.get_tab_name(), '')
