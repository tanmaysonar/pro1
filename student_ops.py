def get_details(name, gender, roll):
	return 'Name: ' + str(name) + '\nGender: ' + str(gender) + '\nRoll: ' + str(roll)

def get_grade(marks):
	if marks >= 70:
		return 'A'
	elif marks >= 60:
		return 'B'
	elif marks >= 40:
		return 'C'
	else:
		return 'Fail'


