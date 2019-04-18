my_lottery = [
   {
   		"name" : "Joseph",
   		"numbers": (0, 1, 2, 3, 4, 5)
   },

    {
   		"name" : "Kang'ethe",
   		"numbers": (6, 7, 8, 9, 10, 11)
   },

    {
   		"name" : "Wamugi",
   		"numbers": (12, 13, 14, 15, 16, 17)
   }
]

print(my_lottery)
print(sum(my_lottery[0]['numbers']))
print(my_lottery[0].total())