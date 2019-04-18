mylist = [0, 1, 2, 3, 4]
print(mylist)

egual_list = [x for x in range(5)]
print(egual_list)

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

print(9 % 2)#if you want to know if a number is odd it will return a 1
print(4 % 2)#if you want to know if a number is even it will return a 0

print([n for n in range(10) if n % 2 ==0]) 
print([n for n in range(10) if n % 2 ==1]) 

knownpeople = ["joseph", " Kangethe ","loise"]
norm_people = [ person.strip().upper() for person in knownpeople ]
print(norm_people)