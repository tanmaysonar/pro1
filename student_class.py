class Student:
	def __init__(self, name, gender, roll, marks):
		self.name = name
		self.gender = gender
		self.roll = roll
		self.marks = marks

	def get_detail(self):
		return 'Name: ' + str(self.name) + '\nGender: ' + str(self.gender) + '\nRoll: ' + str(self.roll)

	def get_name_roll(self):
		return (self.name, self.roll)

	def get_grade(self):
		if self.marks >= 70:
			return 'A'
		elif self.marks >= 60:
			return 'B'
		elif self.marks >= 40:
			return 'C'
		else:
			return 'Fail'


