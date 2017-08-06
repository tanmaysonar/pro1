'''from student_ops import get_details, get_grade


name = str(raw_input('Enter Student Name: '))
gender = str(raw_input('Enter Gender: '))
roll = input('Enter Roll: ')
marks = input('Enter Marks: ')

print get_details(name, gender, roll)
print name + ' got a grade ' + get_grade(marks)
'''

from student_class import Student

s1 = Student('Arun', 'm', 45, 89)
s2 = Student('Karan', 'm', 100, 46)

print s1.get_detail()
print s2.get_detail()


print s1.get_grade()
print s2.get_grade()

tufle = s1.get_name_roll()

for i in tufle:
	print i