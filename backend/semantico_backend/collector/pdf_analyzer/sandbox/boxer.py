from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer
import fitz
import os
import pandas as pd
import pdf2image
import numpy as np
import PIL
from PIL import Image
import io
from pathlib import Path  # it's just my favorite way to handle files
import os

# pdf path
file_path = os.getcwd()
pdf_path = "../../../../output/GWFRN8MA.pdf"
# pdf_path = Path.cwd()/"Git From Bottom Up.pdf"


# PART 1: GET LTBOXES COORDINATES IN THE IMAGE ----------------------
# Open a PDF file.
fp = open(pdf_path, 'rb')

# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)

# Create a PDF document object that stores the document structure.
# Password for initialization as 2nd parameter
document = PDFDocument(parser)

# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources.
manager = PDFResourceManager()

# Create a PDF device object.
# device = PDFDevice(manager)

# BEGIN LAYOUT ANALYSIS
# Set parameters for analysis.
params = LAParams()

# Create a PDF page aggregator object.
device = PDFPageAggregator(manager, laparams=params)

# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(manager, device)


# here is where i stored the data
boxes_data = []
page_sizes = []


def parse_obj(lt_objs, page_nr, verbose=0):
    # loop over the object list
    for obj in lt_objs:
        # if it's a textbox, print text and location
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            if verbose > 0:
                print("%6d, %6d, %s" % (obj.bbox[0], obj.bbox[1], obj.get_text()))
            data_dict = {
                "startX": round(obj.bbox[0]), "startY": round(obj.bbox[1]),
                "endX": round(obj.bbox[2]), "endY": round(obj.bbox[3]),
                "text": obj.get_text(),
                "page_nr": page_nr}
            boxes_data.append(data_dict)
        # if it's a container, recurse
        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs, page_nr)


# loop over all pages in the document
for page_ctr, page in enumerate(PDFPage.create_pages(document)):
    # read the page into a layout object
    interpreter.process_page(page)
    layout = device.get_result()
    # extract text from this object
    parse_obj(layout._objs, page_ctr)
    mediabox = page.mediabox
    mediabox_data = {"height": mediabox[-1], "width": mediabox[-2]}
    page_sizes.append(mediabox_data)

# PART 2: NOW GET PAGE TO IMAGE -------------------------------------
firstpage_size = page_sizes[0]
images = pdf2image.convert_from_path(pdf_path,
                                     poppler_path="/opt/homebrew/Cellar/poppler/23.12.0/bin")
firstpage_image = images[0]

# show first page with the right size (at least the one that pdfminer says)
firstpage_image.show()
firstpage_image.save("data/firstpage.png")

# the magic numbers
dpi = 200/72
vertical_shift = 5  # I don't know, but it's need to shift a bit

# get pages to draw on
doc = fitz.open(pdf_path)
pages = doc.pages()

# loop through boxes (we'll process only first page for now)
for i, _ in enumerate(boxes_data):
    # box data
    startX, startY, endX, endY, text, page_nr = boxes_data[i].values()
    page_height = int(page_sizes[page_nr]["height"] * dpi)

    pages[page_nr].add_text_annot((startX, startY), text)

    # correction PDF --> PIL
    startY = page_height - int(startY * dpi) - vertical_shift
    endY = page_height - int(endY * dpi) - vertical_shift
    startX = int(startX * dpi)
    endX = int(endX * dpi)
    startY, endY = endY, startY

    # turn image into array
    image_array = np.array(images[page])
    # get cropped box
    box = image_array[startY:endY, startX:endX, :]
    convert2pil_image = PIL.Image.fromarray(box)
    # show cropped box image
    # convert2pil_image.show()
    png = "crop_" + str(i) + ".png"
    convert2pil_image.save(png)
    # print this does not match with the text, means there's an error
    print(text)
