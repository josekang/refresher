def who_do_you_know():
	people = input("Enter a list of people: ").upper()
	people_list = people.split(",")
	people_with_no_spaces = []
	for person in people_list:
		people_with_no_spaces.append(person)
	return people_with_no_spaces

def ask_who():
	person = input("Enter the name of the person you know: ").upper()
	if person in who_do_you_know():
		print("You know {} ".format(person))
	else:
		print("You don't know{} ".format(person))
ask_who()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def odd_even():
	even = []
	odd = []
	for number in numbers:
		if number % 2 == 0:
			even.append(number)
		else:
			odd.append(number)
	print(odd,even)
odd_even()