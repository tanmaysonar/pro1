class Author:
	count = 0

	def __init__(self, name, gender, rating):
		self.name = name
		self.gender = gender
		self.rating = rating
		Author.count += 1

	def get_details(self):
		return 'Name: {0}, Gender: {1}, Rating: {2}'.format(self.name, self.gender, self.rating)