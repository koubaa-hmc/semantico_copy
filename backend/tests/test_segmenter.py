import unittest
from semantico_backend.collector.pdf_analyzer.segmenter import Segmentation


class TestSegmenter(unittest.TestCase):
    def test_get_pdfs(self):
        seg = Segmentation()
        response = seg.count_paragraphs('Sowa')
        self.assertEqual("{'Pdfs Count for the description Sowa': '112391'}",
                         response)


if __name__ == '__main__':
    unittest.main()
