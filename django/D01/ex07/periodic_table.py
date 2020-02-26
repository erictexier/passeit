#!/usr/local/bin/python3

DOCHTML = '''<!DOCTYPE html>
<html lang='en'>
<head>
        <title>Periodic Table</title>
        <style>
        table, td, th { 
                border: 1px solid black; 
            }
            #separateTable { 
                border-collapse: separate; 
            } 
            #collapseTable { 
                border-collapse: collapse; 
            }  
        </style>
</head>
<body style="border:1px solid black;">
<table  id = "separateTable">
'''
DOCHTML_END = '''
</table>
</body>
</html>'''

CELL = '''
	<td  bgcolor=pink style="padding:10px">
		<h4>%(name)s</h4>
		<ul>
			<li>No %(number)d</li>
			<li>%(small)s</li>
			<li>%(molar)s</li>
			<li>%(electron)s electron</li>
		<ul>
	</td>
'''

EMPTY_CELL = '''
	<td style="border: 0px solid black; padding:10px">
		
	</td>
'''

def write_cell(f, a):
	for i in a:
		if i == dict():
			f.write(EMPTY_CELL)
		else:
			f.write(CELL % i)

def build_row(position):
	empty = True
	sorted_keys = list(position.keys())
	sorted_keys.sort()
	a = list()
	for i in sorted_keys:
		if position[i] != list():
			if (int(position[i][0]['position']) == i):
				a.append(position[i].pop(0))
			empty = False
		else:
			a.append(dict())
	if empty == False:
		return a
	return ""

def write_html(position):
	f = open("periodic_table.html","w")
	f.write(DOCHTML)
	f.write("<tr>")
	for i in range(len(position)):
		f.write("<th>%d</th>\n" % (i+1))
	f.write("</tr>")

	empty = False
	while(empty == False):
		a = build_row(position)
		if a == "":
			empty = True
		else:
			f.write("<tr>")
			write_cell(f, a)
			f.write("</tr>")

	f.write(DOCHTML_END)

def build_table_position(d):

	position = dict()
	for k in d:
		if (not int(d[k]['position']) in position):
			position[int(d[k]['position'])] = list()
		position[int(d[k]['position'])].append(d[k])
	for i in position:
		position[i] = sorted(position[i], key=lambda x: x['number'],reverse=True)
	return (position)

def build_element(lines):
	d = dict()
	for i in lines:
		line = i.strip()
		temp = line.split("=")
		key = temp[0].strip()
		d[key] = (temp[1].strip()).split(",")
		val = dict()
		for aa in d[key]:
			xx = aa.strip().split(":")
			val[xx[0]]= xx[1]
		val['name'] = key
		val['number'] = float(val['number'])
		d[key] = val
	return d

if __name__ == '__main__':
	f = open("./periodic_table.txt","r")
	lines = f.readlines()
	f.close()
	d = build_element(lines)
	position = build_table_position(d)
	write_html(position)