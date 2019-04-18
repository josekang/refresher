grades = [30, 49, 45, 50, 90]
grades.append(90)
print(grades)

average = (len(grades), "\n", sum(grades), "\n", sum(grades)/len(grades))
print(average)
tuples_grades = (20, 30, 40, 50)##immutable for example it cannot be appended once written
print(tuples_grades)

set_grades= {60,70, 80, 90, 100, 100} ##unique or unodered
print(set_grades)

tuples_grades=tuples_grades+(100,)
print(tuples_grades)

grades[0]=70
print(grades)

set_grades.add(98)
print(set_grades)

##advanced set operations
loterry = {1,2,3,4,5}
winning = {1,6,3,5,7,8,9}
print(loterry.intersection(winning))
print(loterry.union(winning))
print({1, 2, 3, 4}.difference({1, 2}))