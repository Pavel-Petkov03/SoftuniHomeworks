class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
            if user.username in self.rented_books:
                self.rented_books.pop(user.username)
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        find = [user for user in self.user_records if user.user_id == user_id]
        if find:
            actual_object = find[0]
            place = self.user_records.index(actual_object)
            if actual_object.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
            self.user_records[place].username = new_username
            if new_username in self.rented_books:
                self.rented_books.pop(new_username)
            return f"Username successfully changed to: {new_username} for userid: {user_id}"

        return f"There is no user with id = {user_id}!"
