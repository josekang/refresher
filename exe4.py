numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even():
	evens = []
	for number in numbers:
		if number % 2 == 0:
			evens.append(number)
		return evens
even()

def user_menu(choice):
	# choice = input("What is your Choice: ")
	if choice == "q":
		return "Quit"
	elif choice == "a":
		return "Add"

known_people= ["Joseph", "Elizabeth", "Michael"]
# person = input("Enter the person you know: ")

# if person in known_people:
# 	print("You know {}".format(person))
# else:
# 	print("You dont know{}".format(person))

def who_do_you_know():
	# user_input = []
	user_input = input("Write down a list of people you know :")
	user_input = user_input.split()
	print (user_input)
who_do_you_know()
def ask_user():
	person = input("Enter the person you know: ")

	if person in known_people:
		print("You know {}".format(person))
	else:
		print("You dont know{}".format(person))
ask_user()

