class Student():
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	@classmethod
	def new_student(cls,origin, stud_name, *args, **kwargs):
		return cls(stud_name, origin.school,*args, **kwargs)

class workingStudent(Student):
	def __init__(self, name, school, salary, health, job_title, area_work):
		super().__init__(name, school)
		self.salary = salary
		self.job_title = job_title
		self.area_work = area_work
		self.health = health
		
annita = workingStudent("Annita Watiri",  "Oxford University", 80000, "Socially Active", job_title = "Software Engineer", area_work = "Mombasa")
print(annita.name)
print(annita.school)
print(annita.salary)
print(annita.job_title)
print(annita.area_work)
print(annita.health)

new_student = workingStudent.new_student(annita, "Joseph Kang'ethe",90000, "Mentally Fit", job_title = "Software Developer", area_work = "Nairobi")
print(new_student.name)
print(new_student.school)
print(new_student.salary)
print(new_student.job_title)
print(new_student.area_work)
print(new_student.health)
		