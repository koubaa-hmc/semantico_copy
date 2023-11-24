

class Segmentation:
    def __init__(self):
        self.count = -3

    def count_paragraphs(self, path):
        """
        counts the paragraphs in pdf file given by path
        @rtype: int
        """
        return {f"Paragraph Count for the document {path}": str(self.count)}
