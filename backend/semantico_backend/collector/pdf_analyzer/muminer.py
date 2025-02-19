import fitz
from semantico_backend.collector.pdf_analyzer.slico import *


class PdfReader:

    def __init__(self, path):
        self.file_path = path
        self.work_path = make_work_folder(path)

    def extract_text(self):
        with fitz.Document(self.file_path) as doc:  # open document
            text = chr(12).join([page.get_text("text") for page in doc])
        return text

    def extract_paragraphs(self):
        with fitz.Document(self.file_path) as doc:  # open document
            paragraphs = [page.get_text("blocks") for page in doc]
        return paragraphs

    def explore_layout(self, mode):
        """
        Returns blocks
        :param mode: can be rect or k
        :return:
        """
        layout = list()
        if mode == 'rect':
            layout = self._explore_layout_rect()
        elif mode == 'k':
            layout = self._explore_layout_k()
        elif mode == 'w':
            layout = self._explore_layout_word()
        return layout

    def _explore_layout_rect(self):
        # red = (1, 0, 0)
        blue = (0, 0, 1)
        gold = (1, 1, 0)
        # green = (0, 1, 0)
        with fitz.Document(self.file_path) as doc:  # open document
            rects = list()
            for page in doc:
                words = page.get_text("words")
                sorted_words = sorted(words, key=lambda w: (w[1], w[0]))
                for c, word in enumerate(sorted_words):
                    rect = word[:4]
                    pr = str(c) + word[4]
                    rects.append(rect)
                    annot = page.add_freetext_annot(rect, pr, fontsize=4)
                    annot.set_border(width=0.3, dashes=[2])
                    annot.update(text_color=blue, fill_color=gold)
            doc.save(self.file_path + "_ann.pdf")
        return rects

    def _explore_layout_k(self):
        print(f"processing {self.work_path}")
        self.extract_paragraphs()
        png_pages = export_pngs(self.work_path, self.file_path)
        png_segments = export_segments(png_pages)
        return png_segments

    def _explore_layout_word(self):
        """
        For every page the list of words is generated and sorted
        :return: list of words (also a list) per page
        """
        with fitz.Document(self.file_path) as doc:  # open document
            sorted_words = dict()
            for c, page in enumerate(doc, start=1):
                words = page.get_text("words")
                sorted_words[c] = sorted(words, key=lambda w: (w[1], w[0]))
        return sorted_words
