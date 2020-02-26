#!/usr/local/bin/python3
import sys

def capital(val):
	states = {	"Oregon" : "OR",
				"Alabama" : "AL",
				"New Jersey": "NJ",
				"Colorado" : "CO"}
	capital_cities = { 	"OR": "Salem",
						"AL": "Montgomery",
						"NJ": "Trenton",
						"CO": "Denver"}

	for i in capital_cities.items():
		if (i[1] == val and i[0] in states.values()):
			for k in states.items():
				if k[1] == i[0]:
					print (k[0])
			return;

	print("Unknown capital city")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		capital(sys.argv[1])
