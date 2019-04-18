class store():
	def __init__(self, name):
		self.name = name
		self.items = []

	def add_item(self, name, price):
		self.items.append({
			"name" : name,
			"price" : price
		})
		return self.items
	
	def stock_price(self):
		total = 0
		for item in self.items:
			total += item["price"]
		return total


estore1 = store("makenas")
print(estore1.name)
estore1.items = "kuku", "ugali"
estore1.price =200
print(estore1.items)
print(estore1.price)

estore2 = store("Kinyanjuis")
print(estore2.name)
estore2.items = "njugu", "wanyama"
estore2.price = 300
print(estore2.items)
print(estore2.price)

		