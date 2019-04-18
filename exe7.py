##QUESTION ONE########################
student = {
	"name" : "Joseph",
	"school" : "Computing",
	"grades" : (66, 77, 88)
}
print(student)

##QUESTION TWO########################

data = {
	"name" : "Joseph",
	"school" : "Computing",
	"grades" : (66, 77, 88)
}
def average_grades(data):
	grades = data["grades"]
	print(sum(grades))
average_grades(data)

##QUESTION THREE######################
student_list = [
	{
		"name" : "Joseph",
		"school" : "Computing",
		"grades" : (66, 77, 88)
	},
	{
		"name" : "Kang'ethe",
		"school" : "Technology",
		"grades" : (65, 75, 85)
	},
	{
		"name" : "Wamugi",
		"school" : "Enginneering",
		"grades" : (64, 74, 84)
	},
	{
		"name" : "Elizabeth",
		"school" : "Mathematics",
		"grades" : (60, 70, 80)
	}
]

def avarage_grades_students(student_list):
	total = 0
	count = 0
	for stud in student_list:
		total +=  sum(stud["grades"])
		count +=  len(stud["grades"])
	print("Total sum of students grades:",total,"\n","Total number of students grades:",count)
	print("Average:",total / count)


avarage_grades_students(student_list)