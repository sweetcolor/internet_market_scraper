import unittest

from path_manager.files.html_file import HtmlFile


class HtmlFileTestCase(unittest.TestCase):
    def setUp(self):
        self.html_file = HtmlFile()

    def test_csv_extension(self):
        self.assertEqual(self.html_file.ext, 'html')
