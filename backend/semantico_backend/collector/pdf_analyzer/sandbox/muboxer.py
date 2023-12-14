import fitz
import sys


red = (1, 0, 0)
blue = (0, 0, 1)
gold = (1, 1, 0)
green = (0, 1, 0)


def main(*args):
    filename = "../../../output/test_pdf_001.pdf"
    ofile = filename + ".txt"
    doc = fitz.open(filename)
    fout = open(ofile, "wb")

    for page in doc:
        full_text = page.get_text("text")
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda b: (b[1], b[0]))
        for c, b in enumerate(blocks):
            text = b[4].encode("utf-8")
            fout.write(f"{text} at {b[0]}, {b[1]}".encode("utf-8"))
            fout.write("\n".encode("utf-8"))
            r = fitz.Rect(b[0], b[1], b[2], b[3])
            annot = page.add_freetext_annot(r, str(c), fontsize=8)
            annot.set_border(width=0.3, dashes=[2])
            annot.update(text_color=blue, fill_color = gold)
    fout.close()
    doc.save(filename + "_ann.pdf")


if __name__ == "__main__":
    main()