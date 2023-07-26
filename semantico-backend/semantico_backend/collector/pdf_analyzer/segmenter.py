import fitz
import json

class segmentToJson:
    def __init__(self):
        self.count = -1

    def countParagraphs(self):
        return {"ParagraphCount": str(self.count)}