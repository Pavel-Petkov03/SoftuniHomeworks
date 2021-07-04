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
        if user not in self.user_records:
            return "We could not find such user to remove!"
        if user.username in self.rented_books:
            self.rented_books[user.username].remove(user)
        self.user_records.remove(user)

    def change_username(self, user_id, new_username):
        if self.find_user_by_id(user_id):
            current_user = self.find_user_by_id(user_id)[0]
            if current_user.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
            if current_user.username in self.rented_books:
                self.rented_books[new_username] = self.rented_books[current_user.username]
                self.rented_books.pop(current_user.username)
            current_user.username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"

        return f"There is no user with id = {user_id}!"

    def find_user_by_id(self, id_):
        return [user for user in self.user_records if user.user_id == id_]

    @property
    def get_rented_books(self):
        new = []
        for _ , book_and_days in self.rented_books.items():
            ls = list(book_and_days.keys())
            for index in range(len(ls)):
                new.append(ls[index])
        return new
