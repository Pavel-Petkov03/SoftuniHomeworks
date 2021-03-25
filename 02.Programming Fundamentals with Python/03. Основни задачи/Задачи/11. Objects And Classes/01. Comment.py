# Create a class with name "Comment". The __init__ method should accept 3 parameters
# 	username
# 	content
# 	likes (optional, 0 by default)
# Use the exact names for your variables
class Comment:
	def __init__(self , username , content , likes = 0):
		self.username = username
		self.likes = likes
		self.content = content


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)


