from library import Library


class User:
    books = []

    def __init__(self, id_, username):
        self.user_id = id_
        self.username = username

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        if author in library.books_available and book_name in library.books_available[author]:
            if book_name in Library.rented_books:
                return f"The book \"{book_name}\" is already rented and will be available in {Library.rented_books[book_name]} days!"
            library.books_available[author].append(book_name)
            User.books.append(book_name)
            library.rented_books.update({self.username:{book_name:days_to_return}})

    def return_book(self, author: str, book_name: str, library: Library):
        pass


user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2, 'Igor'))
print(library.change_username(12, 'Peter'))
print(library.change_username(12, 'George'))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})

user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
print(library.books_available)
print(library.rented_books)
print(user.books)
