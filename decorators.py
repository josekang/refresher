# DECORATOR -->> a decorator is a function that is called before another function
import functools
def my_decorator(func):
	@functools.wraps(func)
	def function_that_returns_the_func():
		print("I am the DECORATOR")
		func()
		print("I am whom i come before the decorator")
	return function_that_returns_the_func

@my_decorator
def my_function():
	print("I am the actual function")

my_function()