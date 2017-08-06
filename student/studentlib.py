from student import Student

x = 5
s1 = Student('mehul',m,10,89)
s2 = Student('Jane',f, 11,86)

print id(s1)
print id(s2)
print type(s1)
print type(s2)


s1.name = 'Mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 70

s2.name = 'Mehul'
s2.gender = 'f'
s2.roll = 10
s2.marks = 70

print s2.roll
print s1.marks