class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return self.title


class Library:
    def __init__(self):
        self.books = []

    def find_book(self, book):
        if book in self.books:
            return self.books.index(book)
        return f'{book} is not in the library'


HarryPotter = Book('Harry potter', 'J.k')
lb = Library()