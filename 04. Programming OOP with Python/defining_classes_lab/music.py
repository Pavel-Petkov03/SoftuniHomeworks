# Create class named Music that receives title (string), artist (string) and lyrics (string) upon initialization. The class should also have methods print_info() and play().
# The print_info() method should return the following:
# 'This is "{title}" from "{artist}"'
# The play() method should return the lyrics.
# Submit only the class in the judge system. Test your code with your own examples.


class Music:
    def __init__(self, title, artist, lyrics):
        self.lyrics = lyrics
        self.artist = artist
        self.title = title

    def play(self):
        return self.lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())

