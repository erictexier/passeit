#!/usr/local/bin/python3


class intern(object):
	
	class Coffee(object):
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def __init__(self, data="My name? I'm nobody, an intern, I have no name"):
		self.Name = data

	def __str__(self):
		return self.Name

	@staticmethod
	def work():
		raise Exception("I'm just an intern, I can't do that...")

	def make_coffee(self):
		return intern.Coffee()

if __name__ == '__main__':
	p1 = intern("Mark")
	p2 = intern()
	print(p1)
	print(p2)
	p1.make_coffee()
	try:
		p2.work()
	except Exception as e: 
		print(str(e))