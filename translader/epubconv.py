import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


class EpubReader:
    def __init__(self, path):
        self.path = path

    def reader(self):
        book = epub.read_epub(self.path)
        chapters = []
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                chapters.append(item.get_content())
        return chapters

    @staticmethod
    def chap2text(chap):
        blacklist = ['[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script']
        output = ''
        soup = BeautifulSoup(chap, 'html.parser')
        text = soup.find_all(text=True)
        for t in text:
            if t.parent.name not in blacklist:
                output += f'{t} '
        return output

    def convert(self):
        res = ''
        chaps = self.reader()
        for chap in chaps:
            res += self.chap2text(chap)
        return res


if __name__ == "__main__":
    print("Please run 'translader.py'")
