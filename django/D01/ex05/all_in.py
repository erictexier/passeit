#!/usr/local/bin/python3
import sys

states = {	"Oregon" : "OR",
			"Alabama" : "AL",
			"New Jersey": "NJ",
			"Colorado" : "CO"}
capital_cities = { 	"OR": "Salem",
					"AL": "Montgomery",
					"NJ": "Trenton",
					"CO": "Denver"}

def a_state(val):
	for i in capital_cities.items():
		if (i[1] == val and i[0] in states.values()):
			for k in states.items():
				if k[1] == i[0]:
					return (k[0])
	return ""

def capital(us_state):
	if us_state in states and states[us_state] in capital_cities:
		return (capital_cities[states[us_state]])
	return ""

if __name__ == '__main__':
	if len(sys.argv) == 2:
		read = sys.argv[1].split(",")
		for i in read:
			i = i.strip()
			if (i == ""):
				continue
			a = "".join(i.split());
			a = a.capitalize()
			if a in states or a in states.values():
				print (i," is a state")
			elif a in capital_cities.values():
				print (i," is a capital of", a_state(a))
			else:
				print(i,"is neither a capital city nor a state")	
