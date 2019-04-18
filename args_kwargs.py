##args
def my_method(arg1 ,arg2):
	return arg1 + arg2
my_method(0, 0)
print(my_method(10,5))

def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
	return arg1 + arg2 + arg3 + arg4 + arg5 + arg6
my_long_method(0,0,0,0,0,0)
print(my_long_method(1,2,3,4,5,6))

def my_list_addition(list_arg):
	return sum(list_arg)
my_list_addition([1,2,3,4])
print(my_list_addition([3,4,5,6]))

def addition_simplified(*arg):
	return sum(arg)
addition_simplified()
print(addition_simplified(3,4,5,6))

###kwargs
def what_are_kwargs(*arg, **kwargs):
	print(arg)
	print(kwargs)
	print("The avarage of the given list is: {0:.4f}".format(sum(arg) / len(arg)))
what_are_kwargs(10,10,10,10,10,10, name="Joseph Kangethe", location="kawangware")

###the above program is similar to writing
def what_are_kwargs_2(name, location):
	print(name)
	print(location)
what_are_kwargs_2("Wamugi", "Ruai")


