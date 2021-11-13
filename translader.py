import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from translader.Boxtext import BoxText
from translader.translating import translations
from translader.settings import Settings
from translader.epubconv import EpubReader
from translader.pdfconv import pdf_converter


class Application(ttk.Frame):
    """Main application window"""
    def __init__(self, master: tk.Tk):
        super(Application, self).__init__(master)
        self.master = master
        self.panel = None
        self.status_bar = None
        self.text_box = None
        self.text_container = None
        self.filename = None
        self.grid(row=0, column=0, sticky=(tk.N + tk.W + tk.E + tk.S))
        self.settings = Settings()
        self.create_widgets()

    def create_widgets(self):
        """subwindows creator"""
        '''Status bar'''
        status_bar = ttk.Label(self)
        status_bar.grid(row=1, column=0, columnspan=2, sticky=(tk.N, tk.W))

        '''Text box'''
        text_box = BoxText(settings=self.settings, master=self, highlightthickness=0, wrap='word')
        text_box.bind('<Button-3>', self.transl_filler)
        text_box.grid(row=0, column=0, sticky=(tk.N + tk.W + tk.E + tk.S))

        '''Left side panel with translations'''
        panel = ttk.Frame(self)
        panel.grid(row=0, column=1, sticky=(tk.N + tk.W + tk.E + tk.S))

        translate_panel_label = tk.Label(panel, text='Translations', width=32)
        translate_panel_label.grid(row=0, sticky=tk.N)

        '''Menu bar'''
        menubar = tk.Menu()
        # File
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='Open...', command=self.open_file_handler)
        menubar.add_cascade(label='File', menu=file_menu)
        # View
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label='Font +', command=text_box.font_increase, accelerator='Ctrl++')
        view_menu.add_command(label='Font -', command=text_box.font_decrease, accelerator='Ctrl+-')
        menubar.add_cascade(label='View', menu=view_menu)
        self.master.configure(menu=menubar)

        '''Configuring size'''
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        '''Attributes'''
        self.panel = panel
        self.status_bar = status_bar
        self.text_box = text_box

        self.master.bind('<Control-equal>', lambda _: self.text_box.font_increase())
        self.master.bind('<Control-minus>', lambda _: self.text_box.font_decrease())

    def open_file_handler(self):
        self.filename = askopenfilename()
        if self.filename.endswith('.txt'):
            try:
                with open(self.filename, encoding='utf8') as f:
                    text = f.read()
                self.text_box.set_text(text)
                self.text_container = BoxText(settings=self.settings, master=self, highlightthickness=0, wrap="word")
            except UnicodeDecodeError:
                messagebox.showerror('Error', f'error: couldn\'t read file at "{self.filename}", need UTF-8')
        elif self.filename.endswith('.pdf'):
            data = pdf_converter(self.filename)
            self.text_box.set_text(data)
        elif self.filename.endswith('.epub'):
            data = EpubReader(self.filename).convert()
            self.text_box.set_text(data)
        else:
            messagebox.showerror('Error', f'error: invalid file type at "{self.filename}"')

    def transl_filler(self, event: tk.Event):
        selection = self.text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
        result = translations(selection)
        res_menu = ScrolledText(self.panel, width=32, wrap='word', font='Georgia')
        res_menu.grid(row=1, column=0, sticky=(tk.N + tk.S))
        res_menu.delete(0.0, END)
        res_menu.insert(0.0, result)
        res_menu.configure(state='disabled')


if __name__ == '__main__':
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file="icon.png"))
    root.title('Translader')
    app = Application(root)
    mainloop()
