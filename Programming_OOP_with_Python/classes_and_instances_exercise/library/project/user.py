class User:

    def __init__(self, id_, username):
        self.user_id = id_
        self.username = username
        self.books = []

    def get_info_if_is_rented(self, book_name, library):
        for user, value in library.rented_books.items():
            for book, _ in value.items():
                if book == book == book_name:
                    return True
        return False

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if self.get_info_if_is_rented(book_name, library):
            return f"The book \"{book_name}\" is already rented and will be available in {days_to_return} days!"
        if author in library.books_available and book_name in library.books_available[author]:
            library.books_available[author].remove(book_name)
            if book_name not in self.books:
                self.books.append(book_name)
            if self.username in library.rented_books and book_name in library.rented_books[self.username]:
                library.rented_books[self.username].update({book_name: days_to_return})
            else:
                library.rented_books[self.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name in self.books:
            if self.username in library.rented_books and book_name in library.rented_books[self.username]:
                library.rented_books[self.username].pop(book_name)
            library.books_available[author].append(book_name)
            self.books.remove(book_name)

        return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

