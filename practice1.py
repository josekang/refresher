VAT = 0.5
GAT = 2.1
VTA = 1.6

orederamout = float(input("Enter the order amount:"))

country = input("Enter the country you come from: ").upper()
if country == "KENYA":
	province = input("Which provice are you odering from: ").upper()
	if province == "NAIROBI":
		totalorder= orederamout + (VAT*GAT*VTA)
		print("your total charges amounts to: {0:.2f}".format(totalorder))
	else:
		totalorder = orederamout+(VAT*GAT)
		print("your total charges amounts to: {0:.2f}".format(totalorder))
if country != "KENYA":
	totalorder = orederamout + 0
	print("your total charges amounts to: {0:.2f}".format(totalorder))


guests = []
guest =input("Please enter the names of the guests: ")
for guest in guests:
	print(guest)


# def who_do_you_know():
# 	people = input("Enter the name of the guests you know: ")
# 	people_list = people.split(",")
# 	people_nospace =  
