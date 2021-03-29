from user import User


class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def add_user(self, user: User):
        if user not in Library.user_records:
            Library.user_records.append(user)
        else:
            return f"User with id = {user.id} already registered in the library!"

    def remove_user(self, user: User):
        if user in Library.user_records:
            Library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"
        # rented books later

    def change_username(self, user_id: int, new_username: str):
        pass
