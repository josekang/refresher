textcont = True
if textcont:
	print("hello")


knownpeople = ["Joseph", "Elizabeth", "Michael"]
userinput = input("Who do you know: ").capitalize()
if userinput in knownpeople:
	print("Hey you know {}".format(userinput))

# if userinput not in knownpeople:
# 	print("You don't know this person")
else:
	print("Youy don't know {}".format(userinput))

