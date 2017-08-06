class Student:
	def __init__(self, name, gender, roll, marks):
		self.name = name
		self.gender = gender
		self.roll = roll
		self.marks = marks

	def get_grade(self):
			marks = self.marks
		if marks >= 70:
	    	return 'A'
		elif marks >= 60:
	    	return 'B'
		elif marks >= 40:
	    	return 'C'
		else:
	    	return 'Fail'
