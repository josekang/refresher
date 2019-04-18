my_numbers = {1, 2, 3, 4, 5}
print(my_numbers)

######

my_family_memebers = [
     {
         "Name" : "Joseph",
         "Gender" : "Male",
         "Age": 21
     },

     {
     	 "Name" : "Lucy",
         "Gender" : "FeMale",
         "Age": 30
     },

     {
     	"Name" : "Elizabeth",
        "Gender" : "FeMale",
        "Age": 45
     },
     
     {
     	"Name" : "Michael",
        "Gender" : "FeMale",
        "Age": 50
     },

     {
     	"Name" : "Annita",
        "Gender" : "FeMale",
        "Age": 10
     }
]

print(my_family_memebers)
print("@@@@@@@@@@@@@@@@@@@@@@@@@")
my_family_memebers.append(
	       {
	         "Name" : "Trizah",
	         "Gender" : "FeMale",
	         "Age" : 23
	       }
	)

print(my_family_memebers[5])
print(my_family_memebers)

###########

my_lottery = {
	
		"Name" : "Clive",
		"Numbers" : (0, 1, 2, 3, 4)
	
}

print(my_lottery)
print(sum(my_lottery["Numbers"]))
my_lottery["Name"] = ["Victor"]
print(my_lottery)
