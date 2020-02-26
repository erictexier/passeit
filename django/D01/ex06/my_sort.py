#!/usr/local/bin/python3

def my_function():
	d = {
	'Hendrix' : '1942',
	'Allman' : '1946',
	'King' : '1925',
	'Clapton' : '1945',
	'Johnson' : '1911',
	'Berry' : '1926',
	'Vaughan' : '1954',
	'Cooder' : '1947',
	'Page' : '1944',
	'Richards' : '1943',
	'Hammett' : '1962',
	'Cobain' : '1967',
	'Garcia' : '1942',
	'Beck' : '1944',
	'Santana' : '1947',
	'Ramone' : '1948',
	'White' : '1975',
	'Frusciante': '1970',
	'Thompson' : '1949',
	'Burton' : '1939',
	}

	a = list(d.values())
	a = list(set(a))
	a.sort()
	res = dict()
	for i in a:
		if not i in res:
			res[i] = list()
		for k in d:
			if d[k] == i and not k in res[i]:
				res[i].append(k)
	for i in a:
		res[i].sort();
		print (i, " ".join(res[i]))

if __name__ == '__main__':
	my_function()