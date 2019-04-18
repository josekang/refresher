class Student():
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.grades = []

	def average(self):
		return sum(self.grades) / len(self.grades)
		
	@classmethod
	def add_friend(cls, origin, new_name, salary):
		return cls(new_name, origin.school, salary)

#####
class workingStudent(Student):
	def __init__(self, name, school, salary):
		 super().__init__(name, school)
		 self.salary = salary
	

jose = workingStudent("Joseph Kangethe", "Zetech University", 4500)
print(jose.name)
print(jose.salary)

add_friend = workingStudent.add_friend(jose, "Annita", 2400)
print(add_friend.name)
print(add_friend.school)
print(add_friend.salary)





	

		