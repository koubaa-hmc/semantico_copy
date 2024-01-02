import os

from semantico_backend.collector.pdf_analyzer.muminer import PdfReader as MuMiner
from semantico_backend.collector.pdf_analyzer.spoker import Worph as Word
from semantico_backend.collector.pdf_analyzer.spoker import Plumph as Paragraph


def test_create_words():
    pdf_folder_path = "../output/essai_002"
    pdf_paths = [path for path in os.listdir(pdf_folder_path) if os.path.splitext(path)[1] == ".pdf"]
    reader = MuMiner(os.path.join(pdf_folder_path, pdf_paths[0]))
    page_words = reader.explore_layout(mode='w')
    for page_word in page_words:
        for word in page_words[page_word]:
            bound = {'lt': (word[0], word[1]), 'rb': (word[2], word[3])}
            Word(pdf_ui='W47UA76J', page=page_word, boundary=bound, text=word[4])
    assert True


def test_create_word():
    bound = {'lt': (0, 1), 'rb': (2, 2)}
    my_test_word = Word(pdf_ui='H4D9BJ9P', page=1, boundary=bound, text="John")
    assert('', my_test_word)


def test_create_paragraph():
    bound = {'lt': (0, 1), 'rb': (2, 2)}
    my_test_paragraph = Paragraph(pdf_ui='H4D9BJ9P', page=1, boundary=bound)
    assert('', my_test_paragraph)
