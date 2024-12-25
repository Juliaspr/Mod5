import json
class Model:
    title = str
    text = str
    author = str


    def __init__(self, title:str, text: str,  author: str):
        self.title = title
        self.author = author
        self.text = text

    def get_title(self):
        return self.title

    def set_title(self, title:str):
        self.title = title

    def get_text(self):
        return self.text

    def set_text(self, text: str):
        self.text = text

    def get_author(self):
        return self.author

    def set_author(self, author: str):
        self.author = author


def save(title:str, text:str, author:str):
    dictionary = {"title": title, "text ":  text, "author": author}
    with open('1.json', 'a') as f:
        json.dump(dictionary, f)

s = Model("ggg", "fff", "eee")
save(s.get_title(), s.get_text(),s.author)

print(s.get_author(),s.get_title(),s.get_text())


