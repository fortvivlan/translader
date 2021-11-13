# translader

### Version 0.1

Translader is a very simple GUI program which can interactively look up for Google translations while reading texts.

### How to run it

You have to have Python (presumably it must be version 3.8, though I haven't checked) and all packages under Dependencies. Open console in the folder with 'translader.py' and run the following:

    python translader.py
    

### Dependencies:

    pip install beautifulsoup4
    pip install EbookLib
    pip install googletrans==3.1.0a0
    pip install pdfminer.six


### What it can

<ul>
    <li>open files and display them as raw text. Supported formats:</li>
        <ul>
            <li>.txt, encoding: UTF-8</li>
            <li>.epub</li>
            <li>.pdf (beware: results will be mostly poor)</li>
        </ul>
    <li>increase and descrease font size</li>
    <li>get google translations on right click on selection (Windows-checked only, doesn't work on MacOS, garanteed)</li>
    <li>Google makes guesses about source language</li>
    <li>your destination language will be most probably English</li>
</ul>

### What's planned for future

<ul>
    <li>add .docx support (more dependencies tho)</li>
    <li>add .doc support (still more dependencies)</li>
    <li>add the option to choose source language</li>
    <li>add the option to choose destination language</li>
    <li>add the ability to memorize scrollbar position</li>
    <li>add the ability to copy selected text</li>
    <li>and, perhaps, to create dictionary out of collected translations</li>
</ul>


Special thanks to vdobrovolskii
