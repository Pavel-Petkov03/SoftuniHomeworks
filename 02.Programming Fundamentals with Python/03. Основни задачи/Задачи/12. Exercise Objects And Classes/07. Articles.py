# Create a class Article. The __init__ method should accept 3 arguments:
# title, content, author. The class should also have 4 methods:
# n	edit(new_content) - chages the old content to the new one
# 	change_author(new_author) - changes the old author to with the new one
# rename(new_title) - changes the old title with the new one
# 	__repr__() - returns the following string "{title} - {content}: {author}"


class Article:
	def __init__(self, title, content, author):
		self.title = title
		self.content = content
		self.author = author

	def edit(self, new_content):
		self.content = new_content

	def change_author(self, new_author):
		self.author = new_author

	def rename(self, new_title):
		self.title = new_title

	def __repr__(self):
		return f'{self.title} - {self.content}: {self.author}'


article = Article("some title", "some content", "some author")
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)



