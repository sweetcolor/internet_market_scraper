import unittest

from path_manager.files.jpeg_file import JpegFile


class JpegFileTestCase(unittest.TestCase):
    def setUp(self):
        self.jpeg_file = JpegFile()

    def test_csv_extension(self):
        self.assertEqual(self.jpeg_file.ext, 'jpeg')
