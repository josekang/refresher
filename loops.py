mytext = "Jesus Christ"
# print(mytext[0])
# print(mytext[1])
# print(mytext[2])
# print(mytext[3])
# print(mytext[4])
# print(mytext[5])
# print(mytext[6])
# print(mytext[7])
for text in mytext:
	print(text)

mylist = [1, 2, 3, 4, 5]
# print(mylist[0])
for num in mylist:
	print(num **2)

userneed = True
while userneed == True:
	print(10)

	userinput = input("Should we print again (y/n)?: ")
	if userinput == "n":
		userneed = False