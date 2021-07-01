class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    @staticmethod
    def print_line_of_slashes():
        return '-----------'

    def display(self):
        result = ''
        for page in range(self.pages):
            result += f'{self.print_line_of_slashes()}\n'
            result += f'{" ".join(["[]" for _ in range(len(self.photos[page]))])}\n'
        result += f'{self.print_line_of_slashes()}\n'
        return result



