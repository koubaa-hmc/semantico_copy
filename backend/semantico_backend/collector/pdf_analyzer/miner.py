from pdfminer.high_level import extract_text


class PdfReader:
    def __init__(self, path):
        self.path = path

    def extract_text(self):
        return extract_text(self.path)
