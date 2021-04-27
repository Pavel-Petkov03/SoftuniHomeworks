
class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        find = [a for a in self.albums if a.name == album_name]
        if find:
            initial_album = find[0]
            if initial_album.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(initial_album)
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f'Band {self.name}\n'
        for alb in self.albums:
            result += alb.details()
        return result




