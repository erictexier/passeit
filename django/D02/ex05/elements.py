#!/usr/bin/env python3

from elem import Elem,Text

class Html(Elem):
	def __init__(self, a_list):
		super(Html, self).__init__( tag='html',
									content= a_list,
									attr={'lang':'en'})
	def __str__(self):
		return "<!DOCTYPE html>\n" + super(Html,self).__str__()

class Head(Elem):
	def __init__(self, a_list=None):
		super(Head, self).__init__( tag='head',
									content=a_list)

class Title(Elem):
	def __init__(self, text):
		super(Title, self).__init__( tag='title',
									content=[Text(text)])

class Body(Elem):
	def __init__(self, a_list=None):
		super(Body, self).__init__( tag='body',
									content=a_list)

class H1(Elem):
	def __init__(self, text):
		super(H1, self).__init__( tag='H1', content=Text(text))

class Img(Elem):
	def __init__(self, src):
		super(Img, self).__init__( tag='img', attr={'src':src})

if __name__ == '__main__':
	print( Html( [	Head(Title("page bonjour")), 
					Body([H1("hello"),Img("http://i.imgur.com/pfp3T.jpg")])
				] ))

