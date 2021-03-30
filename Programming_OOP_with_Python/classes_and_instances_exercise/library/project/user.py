
class User:
    books = []
    def __init__(self,id_,username):
        self.user_id = id_
        self.username = username

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if author in library.books_available and book_name in library.books_available[author]:
            if self.username in library.rented_books and book_name in library.rented_books[self.username]:
                library.rented_books[self.username][book_name] = days_to_return
                return f"The book \"{book_name}\" is already rented and will be available in {days_to_return} days!"
            library.books_available[author].remove(book_name)
            User.books.append(book_name)
            library.rented_books[self.username] = {book_name : days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author:str, book_name:str, library):
        if book_name in User.books:
            library.rented_books[self.username].pop(book_name)
            library.books_available[author].remove(book_name)

        return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ', '.join([])

    def __str__(self):
        return f"{self.user_id}, {self.username}, {User.books}"




