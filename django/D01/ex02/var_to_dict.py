#!/usr/local/bin/python3

def print_list(t):
	d = dict()
	for i in t:
		if not i[1] in d:
			d[i[1]] = list()
		d[i[1]].append(i[0])
	for i in d:
		print (i,":",d[i][0])


if __name__ == '__main__':
	d = [	('Hendrix' , '1942'),
			('Allman' , '1946'),
			('King' , '1925'),
			('Clapton' , '1945'),
			('Johnson' , '1911'),
			('Berry' , '1926'),
			('Vaughan' , '1954'),
			('Cooder' , '1947'),
			('Page' , '1944'),
			('Richards' , '1943'),
			('Hammett' , '1962'),
			('Cobain' , '1967'),
			('Garcia' , '1942'),
			('Beck' , '1944'),
			('Santana' , '1947'),
			('Ramone' , '1948'),
			('White' , '1975'),
			('Frusciante', '1970'),
			('Thompson' , '1949'),
			('Burton' , '1939')
		]
	print_list(d)