import unittest
from semantico_backend.collector.pdf_analyzer.miner import PdfReader


class TestMiner(unittest.TestCase):
    def test_extract_text(self):
        reader = PdfReader("/Users/ot2661/Documents/01_dev/semantico/backend/output/H4D9BJ9P.pdf")
        text = reader.extract_text()
        self.assertEqual("", text)


if __name__ == '__main__':
    unittest.main()
