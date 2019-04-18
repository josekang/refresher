#####USING CLASES TO SOLVE COMPOLEX OBJECTS FOR EXAMPLE A GROUP OF STUDENTS
class students():
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.grades = []

	def average_grades(self):
		return sum(self.grades) / len(self.grades)

jose = students("Joseph Kangethe", "Zetech University")
print(jose.name)
print(jose.school)
jose.grades = [50, 60, 70, 80]
jose.grades.append(90)
print(jose.grades)
print(jose.average_grades())























