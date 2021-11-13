from pdfminer.high_level import extract_text


def pdf_converter(path):
    return extract_text(path)


if __name__ == "__main__":
    print("Please run 'translader.py'")
