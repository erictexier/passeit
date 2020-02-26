#!/usr/local/bin/python3


class HotBeverage(object):
	def __init__(self):
		self.price = .30
		self.name = 'hot beverage'
	def description(self):
		return "Just some hot water in a cup"
	def __str__(self):
		return ("name: {0}\nprice: {1:.2f}\ndescription: {2}".format(	self.name,
																		self.price,
																		self.description()))

class Coffee(HotBeverage):
	def __init__(self):
		super(Coffee,self).__init__()
		self.name = "coffee"
		self.price = 0.4
	def description(self):
		return "Coffee in a cup"

class Tea(HotBeverage):
	def __init__(self):
		super(Tea,self).__init__()
		self.name = "tea"

class Chocolate(HotBeverage):
	def __init__(self):
		super(Chocolate,self).__init__()
		self.name = "chocolate"
		self.price = .5
	def description(self):
		return "Hot chocolate"

class Cappuccino(HotBeverage):
	def __init__(self):
		super(Cappuccino,self).__init__()
		self.name = "cappuccino delicious"
		self.price = .45



if __name__ == '__main__':
	for i in [HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino()]:
		print(i)