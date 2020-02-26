#!/usr/local/bin/python3
import sys

def capital(us_state):
	states = {	"Oregon" : "OR",
				"Alabama" : "AL",
				"New Jersey": "NJ",
				"Colorado" : "CO"}
	capital_cities = { 	"OR": "Salem",
						"AL": "Montgomery",
						"NJ": "Trenton",
						"CO": "Denver"}

	if us_state in states and states[us_state] in capital_cities:
		print(capital_cities[states[us_state]])
	else:
		if not us_state in states:
			print("unknown state")
		else:
			print("Unknown capital city")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		capital(sys.argv[1])
