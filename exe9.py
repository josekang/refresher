class Store():
 	def __init__(self, name):
 		self.name = name
 		self.item = []

 		def add_item(self, name, price):
 			self.items.append(
 				{
 					"name" : name,
 					"price" : price
 				})
 			return self.items
 			
 		def store_price(self):
 			return sum(item["price"] for item in self.items)

 		@classmethod
 		def franchise(cls, Storree):
 			return Store(Storree.name + " - franchise")

 		@staticmethod
 		def store_details():
 			return "{}, total stock price {}".format(Storree.name, int(store_price()))

estore = Store("makenas")
print(estore.name)
estore.price = 200

