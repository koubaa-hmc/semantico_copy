import unittest
from semantico_backend.collector.pdf_analyzer.miner import PdfReader as Miner
from semantico_backend.collector.pdf_analyzer.muminer import PdfReader as AdvMiner
from semantico_backend.collector.pdf_analyzer.muminer import PdfReader as MuMiner


class TestMiner(unittest.TestCase):
    def test_extract_text(self):
        reader = MuMiner("/Users/ot2661/Documents/01_dev/semantico/backend/output/pdffile_002.pdf")
        text = reader.extract_text()
        # self.assertEqual("", text)
        paragraphs = reader.extract_paragraphs()
        self.assertEqual("", paragraphs)

    def test_explore_layout(self):
        reader = MuMiner("/Users/ot2661/Documents/01_dev/semantico/backend/output/H4D9BJ9P.pdf")
        text = reader.explore_layout()
        self.assertEqual("", text)

    def test_adv_extract_text(self):
        reader = AdvMiner("/Users/ot2661/Documents/01_dev/semantico/backend/output/H4D9BJ9P.pdf")
        text = reader.extract_text()
        self.assertEqual("", text)

    def test_adv_explore_layout(self):
        reader = AdvMiner("/Users/ot2661/Documents/01_dev/semantico/backend/output/H4D9BJ9P.pdf")
        text = reader.explore_layout()
        self.assertEqual("", text)


if __name__ == '__main__':
    unittest.main()
