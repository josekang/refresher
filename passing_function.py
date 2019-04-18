def parentMethod(result):
	return result()

def multiply_two_numbers():
	a = 10
	b = 10
	c = a * b
	return c

print(parentMethod(multiply_two_numbers))

##how to use the lamba function
print(parentMethod(lambda:10 * 10))

##now here is the importance of passing fonctions as arguments
my_marks = [40, 50, 60, 70, 80]
my_marks.remove(40)
print(my_marks)

###here is why1 -- the use of filter
my_grades = [90, 100, 200, 300, 400]
print(list(filter(lambda x: x!=300, my_grades)))

##here is why2
def not_400(x):
	return x != 400
print(list(filter(not_400, my_grades)))

###here is why3 the use list comprehension
print([x for x in my_grades if x != 200])

print((lambda x: x * 3)(5))

