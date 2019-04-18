###A LOOK ON THE DIFFERENCE OF USING CLASSES AND NOT USING

####HERE IS A DICTIONERY WITHOUT THE USE OF CLASSES AND OBJECTS
lottery_dic = {
	"name" : "Joseph",
	"numbers" : (1, 2, 3, 4, 5)
}
print(lottery_dic)

###HOW TO CREATE CLASSES
class lottery():
	def __init__(self, name):
		self.name = name
		self.numbers = (16,17, 18, 19, 20)
	def total(self):
		return sum(self.numbers)

player1 = lottery("Joseph")
player2 = lottery("lucy")
player1.numbers = (6, 7, 8, 9, 10)
player2.numbers = (11, 12, 13, 14, 15)
print(player1.name)
print(player1.numbers)
print(player2.name)
print(player2.numbers)
print(player1.total())