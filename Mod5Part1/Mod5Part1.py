class SpringVar:
    text: str

    def __init__(self,text: str):
        self.set(text)

    def set(self, text: str):
        self.text = text

    def get(self):
        return print(self.text)


if __name__ == '__main__':
    s = SpringVar("hi")
    s.get()
    s.set("test")
    s.get()



