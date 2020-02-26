from django.shortcuts import render
from django.http import HttpResponse
from ex00 import create_database
# Create your views here.

def init(request):
	table = "ex00_movies"
	if create_database.do_it_make_table(table):
		return HttpResponse("OK")
	return HttpResponse("OK: table ex00_movies exist already")