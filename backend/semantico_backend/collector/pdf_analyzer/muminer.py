import fitz


class PdfReader:
    def __init__(self, path):
        self.path = path

    def extract_text(self):
        with fitz.open(self.path) as doc:  # open document
            text = chr(12).join([page.get_text("text") for page in doc])
        return text

    def extract_paragraphs(self):
        with fitz.open(self.path) as doc:  # open document
            paragraphs = [page.get_text("blocks") for page in doc]
        return paragraphs

    def explore_layout(self):
        pass

