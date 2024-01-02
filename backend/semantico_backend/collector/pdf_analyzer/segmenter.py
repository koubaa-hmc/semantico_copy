import logging

from semantico_backend.collector.zotero.adv_interface import ZoteroInterface
from semantico_backend.collector.pdf_analyzer.muminer import PdfReader

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class Segmentation:
    def __init__(self):
        self.count = 0
        self.zi = ZoteroInterface('user')
        self.item_desc = ''
        self.file_paths = []

    def set_file_paths(self, item_desc):
        if not self.file_paths or not(item_desc == self.item_desc):
            self.file_paths = self.zi.get_pdfs(item_desc)
            self.item_desc = item_desc
        count_documents = len(self.file_paths)
        return {f"Number of documents found for the desc {item_desc}": count_documents}

    def count_paragraphs(self, item_desc):
        """
        counts the paragraphs in pdf file given by item_desc
        :param item_desc: string to be quick searched (Auth., Title, etc.)
        :return: count of paragraphs
        """
        self.set_file_paths(item_desc)
        count_paragraphs = 0
        for file_path in self.file_paths:
            reader = PdfReader(file_path)
            paragraphs = reader.extract_paragraphs()
            count_paragraphs += len(paragraphs)

        return {f"Count of paragraphs for the description {item_desc}": count_paragraphs,
                "found in (nb of files)": len(self.file_paths)}

    def display_paragraphs(self, item_desc):
        """
        display the paragraphs in pdf file given by item_desc
        :param item_desc: string to be quick searched (Auth., Title, etc.)
        :return: list of paragraphs
        """
        self.set_file_paths(item_desc)
        paragraphs = ''
        for file_path in self.file_paths:
            reader = PdfReader(file_path)
            paragraphs = reader.extract_paragraphs()

        return {f"The paragraphs for the description {item_desc}": paragraphs,
                "found in (nb of files)": len(self.file_paths)}

    def explore_layout(self, item_desc):
        """
        display the layout objects with corresponding coordinates
        :param item_desc: string to be quick searched (Auth., Title, etc.)
        :return: dictionary of layout objects
        """
        self.set_file_paths(item_desc)
        d_layout = dict()
        for file_path in self.file_paths:
            reader = PdfReader(file_path)
            d_layout = reader.explore_layout('rect')

        return d_layout
