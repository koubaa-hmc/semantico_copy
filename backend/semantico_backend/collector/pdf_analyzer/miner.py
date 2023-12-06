from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTFigure, LTTextBox
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser


class PdfReader:
    def __init__(self, path):
        self.path = path

    def extract_text(self):
        with open(self.path, 'rb') as f:
            parser = PDFParser(f)
            doc = PDFDocument(parser)
            page = list(PDFPage.create_pages(doc))[0]
            rsrcmgr = PDFResourceManager()
            device = PDFPageAggregator(rsrcmgr, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            interpreter.process_page(page)
            layout = device.get_result()
            text = ""
            for obj in layout:
                if isinstance(obj, LTTextBox):
                    text += obj.get_text()

        return text
