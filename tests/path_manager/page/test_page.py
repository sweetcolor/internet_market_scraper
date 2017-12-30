import unittest

from path_manager.page.page import Page
from path_manager.page.root_page import RootPage


class PageTestCase(unittest.TestCase):
    def setUp(self):
        self.page1 = Page('https://hard.rozetka.com.ua/processors/c80083/',
                          RootPage('https://hard.rozetka.com.ua/'))
        self.page2 = Page('https://hard.rozetka.com.ua/intel_core_i3_7100/p13244917/',
                          self.page1)

    def test_get_parent_page_link_name(self):
        self.assertEqual(self.page1.get_parent_page_link_name(), 'hard.rozetka.com.ua')
        self.assertEqual(self.page2.get_parent_page_link_name(), 'processors-c80083')
