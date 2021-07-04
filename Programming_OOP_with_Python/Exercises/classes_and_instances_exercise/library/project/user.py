
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            self.add_to_rented(book_name, days_to_return, library)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        elif book_name in library.get_rented_books:
            return f"The book \"{book_name}\" is already rented and will be available in {days_to_return} days!"

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        library.books_available[author].append(book_name)
        library.rented_books[self.username].pop(book_name)
        self.books.remove(book_name)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

    def info(self):
        return ', '.join(sorted(self.books))

    def add_to_rented(self, book_name, days_to_return, library):
        if self.username in library.rented_books:
            library.rented_books[self.username][book_name] = days_to_return
            return
        library.rented_books[self.username] = {book_name: days_to_return}




