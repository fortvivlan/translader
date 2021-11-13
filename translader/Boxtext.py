import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from translader.settings import Settings


class BoxText(ScrolledText):
    def __init__(self, *, settings: Settings, **kwargs):
        super().__init__(**kwargs, font=('Georgia', settings.text_box_font_size))
        self.configure(state='disabled')
        self.tag_configure('sel', underline=True)

        self.settings = settings

    def font_decrease(self):
        if self.settings.text_box_font_size > 8:
            self.settings.text_box_font_size -= 1
            self.configure(font=('Georgia', self.settings.text_box_font_size))

    def font_increase(self):
        self.settings.text_box_font_size += 1
        self.configure(font=('Georgia', self.settings.text_box_font_size))

    def set_text(self, text: str):
        self.configure(state="normal")
        self.delete("1.0", tk.END)
        self.insert("end", text)
        self.configure(state="disabled")


if __name__ == "__main__":
    print("Please run 'translader.py'")
