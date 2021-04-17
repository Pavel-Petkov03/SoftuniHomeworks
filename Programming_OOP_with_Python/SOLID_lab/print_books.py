from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class Printer:
    def __init__(self, book):
        self.book = book

    def get_book(self, wanted_format):
        return wanted_format().format(self.book)


class HTMLFormat(Formatter):
    def format(self, book: Book) -> str:
        return f'<content>{book.content}</content>'


class UpperCaseFormat(Formatter):
    def format(self, book: Book) -> str:
        return book.content.upper()


bk = Book('bg')
pt = Printer(bk)
print(pt.get_book(HTMLFormat))
print(pt.get_book(UpperCaseFormat))
