import json
import os


class Settings:
    def __init__(self):
        if os.path.exists("settings.json"):
            with open("settings.json", mode="r", encoding="utf8") as f:
                self.settings = json.load(f)
        else:
            self.settings = {"text_box_font_size": 14}

    @property
    def text_box_font_size(self) -> int:
        return self.settings["text_box_font_size"]

    @text_box_font_size.setter
    def text_box_font_size(self, value: int):
        self.settings["text_box_font_size"] = value
        self.save()

    def save(self):
        with open("settings.json", mode="w", encoding="utf8") as f:
            json.dump(self.settings, f, indent=4)


if __name__ == "__main__":
    print("Please run 'translader.py'")
