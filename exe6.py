def who_do_you_know():
	people = input("Enter the names of the people you know: ").upper()
	people_list = people.split(",")
	people_nospaces = [person.strip() for person in people_list]
	return people_nospaces

def ask():
	name = input("Enter the name of the person you know: ").upper()
	if name in who_do_you_know():
		print("you know {}".format(name))
	else:
		print("you dont know {}".format(name))
ask()