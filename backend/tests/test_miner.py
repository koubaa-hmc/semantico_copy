import unittest
from semantico_backend.collector.pdf_analyzer.miner import PdfReader as Miner
from semantico_backend.collector.pdf_analyzer.muminer import PdfReader as AdvMiner
from semantico_backend.collector.pdf_analyzer.muminer import PdfReader as MuMiner
import os


class TestMiner(unittest.TestCase):
    def test_extract_text(self):
        pdf_folder_path = "../output/essai_001"
        pdf_paths = os.listdir(pdf_folder_path)
        readers = [MuMiner(os.path.join(pdf_folder_path, pdf_path)) for pdf_path in pdf_paths]
        text = [reader.extract_text() for reader in readers]
        # self.assertEqual("", text)
        paragraphs = [reader.extract_paragraphs() for reader in readers]
        self.assertEqual("", text)
        self.assertEqual("", paragraphs)

    def test_explore_layout_rect(self):
        pdf_folder_path = "../output/essai_001"
        pdf_paths = [path for path in os.listdir(pdf_folder_path) if os.path.splitext(path)[1] == ".pdf"]
        readers = [MuMiner(os.path.join(pdf_folder_path, pdf_path)) for pdf_path in pdf_paths][2:4]  # two pdf
        rects = [reader._explore_layout_rect() for reader in readers]
        self.assertEqual([], rects)

    def test_explore_layout_k(self):
        pdf_folder_path = "../output/essai_005"
        pdf_paths = [path for path in os.listdir(pdf_folder_path) if os.path.splitext(path)[1] == ".pdf"]
        slicos = [MuMiner(os.path.join(os.path.abspath(pdf_folder_path), pdf_path)) for pdf_path in pdf_paths]
        regions = [slico._explore_layout_k() for slico in slicos]
        self.assertNotEqual([], regions)


if __name__ == '__main__':
    unittest.main()
