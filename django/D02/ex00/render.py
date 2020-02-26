#!/usr/local/bin/python3

import sys
import os
import re
import settings

def build_html(template_file):

	out = template_file.replace(".template",".html")
	tfile = open(template_file,"r")
	lines = tfile.readlines()
	tfile.close()
	strlines = "".join(lines)
	for x in dir(settings):
		if not x.startswith("__"):
			key = '{'+x+'}'
			val = settings.__dict__[x]
			print ("{} {}".format(key,val))
			strlines = re.sub(r'%s' % key, r'%s' % val, strlines)
	fout = open(out,"w")
	fout.write(strlines)

if __name__ == '__main__':
	template = ''
	if len(sys.argv) > 2:
		print("too many template file")
		sys.exit(1)
	try:
		template = sys.argv[1]
	except:
		print("No template file in param, using default")
		sys.exit(1)
	build_html(template)