from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


class PdfReader:
    def __init__(self, path):
        self.path = path

    def extract_text(self):
        return extract_text(self.path)

    def extract_paragraphs(self):
        text = self.extract_text()
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
        return paragraphs

    def explore_layout(self):
        output = dict()
        with open(self.path, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            manager = PDFResourceManager()
            params = LAParams()
            device = PDFPageAggregator(manager, laparams=params)
            interpreter = PDFPageInterpreter(manager, device)
            for p, page in enumerate(PDFPage.create_pages(doc), start=100):
                interpreter.process_page(page)
                layout = device.get_result()
                for c, layout_object in enumerate(layout, start=1):
                    if isinstance(layout_object, LTTextBox):
                        x, y, text = layout_object.bbox[0], layout_object.bbox[3], layout_object.get_text()
                        output[p+c] = {"x": x, "y": y, "text": text}
        return output

