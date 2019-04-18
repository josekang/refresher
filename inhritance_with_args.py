class Student():
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	@classmethod
	def new_friend(cls,origin, friend, *arg):
		return cls(friend, origin.school, *arg)


class workingStudent(Student):
	def __init__(self, name, school, salary, job_title):
		super().__init__(name, school)
		self.salary = salary
		self.job_title = job_title

annita = workingStudent("Annita Watiri", "Havard University", 76000, "Software Engineer")
print(annita.name)
print(annita.school)
print(annita.salary)
print(annita.job_title)

new_friend = workingStudent.new_friend(annita, "Joseph Kang'ethe", 80000, "Software Developer")
print(new_friend.name)
print(new_friend.school)
print(new_friend.salary)
print(new_friend.job_title)

new_friend = workingStudent.new_friend(annita, "Clive Ominde", 98000, "Project Manager")
print(new_friend.name)
print(new_friend.school)
print(new_friend.salary)
print(new_friend.job_title)