import fitz
import json

class segmentToJson:
    def __init__(self):
        self.count = -1

    def countParagraphs(self, path):
        return {f"Paragraph Count for the document {path}": str(self.count)}