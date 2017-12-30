import unittest

from path_manager.files.csv_file import CsvFile


class CsvFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv_file = CsvFile()

    def test_csv_extension(self):
        self.assertEqual(self.csv_file.ext, 'csv')
