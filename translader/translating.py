from googletrans import Translator


def translations(text):
    translator = Translator()
    trans = translator.translate(text)
    return trans.text


if __name__ == "__main__":
    print("Please run 'translader.py'")
