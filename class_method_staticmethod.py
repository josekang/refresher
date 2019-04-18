class Student():
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.grades = []

	def average(self):
		return sum(self.grades) / len(self.grades)

	@staticmethod
	def go_to_school():
		print("i am going to school")
	
jose = Student("Joseph Kang'ethe", "Zetech University")
pato = Student("Patrick Lumumba", "Jomo Kenyatta University of Agriculture and technology")

jose.grades = [40, 50, 60, 70]
jose.grades.append(90)
print(jose.name,"\n",jose.school,"\n",jose.grades)
print(jose.average())

pato.grades = [40, 50, 60, 70]
pato.grades.append(90)
print(pato.name,"\n",pato.school,"\n",pato.grades)
print(jose.average())

print(jose.average() * pato.average())

Student.go_to_school()
