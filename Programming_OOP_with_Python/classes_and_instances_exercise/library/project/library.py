


class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def add_user(self, user):
        if user not in Library.user_records:
            Library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user):
        if user in Library.user_records:
            Library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"
        # rented books later

    def change_username(self, user_id: int, new_username: str):
        find = [c for c in Library.user_records if c.user_id == user_id]
        if find:
            user_object = find[0]
            if user_object.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
            Library.rented_books[new_username] = 1
            Library.user_records[Library.user_records.index(user_object)].username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"

        return f"There is no user with id = {user_id}!"