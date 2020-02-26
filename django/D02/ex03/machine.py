#!/usr/local/bin/python3
import random
import beverages

class CoffeeMachine(object):

	def __init__(self):
		super(CoffeeMachine, self).__init__()
		self.countrepair = 0

	class EmptyCup(beverages.HotBeverage):
		def __init__(self):
			super(CoffeeMachine.EmptyCup,self).__init__()
			self.name = "An empty cup?! Gimme me my money back!"
			self.price = 0.90

	class BrokenMachineException(Exception):
		expression = "Broken Machine"
		message = "this coffee machine has to be repair"

		@classmethod
		def __str__(cls):
			return cls.message

	def repair(self):
		self.countrepair = 0

	def serve(self, subclshotbeverage):
		# Obsolescence
		self.countrepair += 1
		if (self.countrepair > 10):
			try:
				raise CoffeeMachine.BrokenMachineException()
			except Exception as e:
				print(e)
				self.repair()

		if ((int)(random.random() * 100 ) % 2):
			return subclshotbeverage()
		return CoffeeMachine.EmptyCup()

if __name__ == '__main__':
	c = CoffeeMachine()
	order = [beverages.Coffee, beverages.Tea, beverages.Chocolate, beverages.Cappuccino]
	for i in range(20):
		index = (int)(random.random() * 100 ) % 4
		print("{}, {}".format(i,c.serve(order[index])))