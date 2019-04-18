import functools
def my_decorator(func):
	@functools.wraps(func)
	def function_returning_func():
		print("I am the DECORATOR")
		func()
		print("I come after the DECORATOR")

	return function_returning_func

@my_decorator
def my_function():
	print("I am the actual function")
my_function()

###
def decorator_that_takes_argument(number):
	def my_decorator(func):
		@functools.wraps(func)
		def function_returning_func(*args, **kwargs):
			print("I am the DECORATOR")
			if number == 56:
				print("Not Running the function")
			else:
				func(*args, **kwargs)
			print("I come after the DECORATOR")
		return function_returning_func
	return my_decorator

@decorator_that_takes_argument(54)
def my_function_two(x, y):
	print(x + y)
	print("Jambo Kenya Hakuna Matata")
my_function_two(50, 50)
