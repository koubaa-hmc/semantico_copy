import logging

from semantico_backend.collector.zotero.adv_interface import ZoteroInterface
from semantico_backend.collector.pdf_analyzer.miner import PdfReader

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Segmentation:
    def __init__(self):
        self.count = -3
        self.zi = ZoteroInterface('user')

    def count_paragraphs(self, item_desc):
        """
        counts the paragraphs in pdf file given by item_desc
        """
        file_paths = self.zi.get_pdfs(item_desc)
        first_file_path = file_paths[0]

        reader = PdfReader(first_file_path)
        text = reader.extract_text()

        return {f"Pdf text for the description {item_desc}": text}
