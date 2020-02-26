from django.shortcuts import render
from django.http import HttpResponse
from ex00 import create_database

table = "ex02_movies"

# Create your views here.
def init(request):
	if create_database.do_it_make_table(table):
		return HttpResponse("OK")
	return HttpResponse("OK: table ex02_movies exist already")

def populate(request):
    conn = create_database.get_connection('localhost','formationdjango', 'djangouser', 'secret')
    if conn == None or not create_database.table_exist(conn, table):
        return HttpResponse("No data available")

    cur = conn.cursor()
    rep = list()
    list_film = create_database.DefaultTable()
    for film in list_film:
        title = film.get('title', None)
        ok = True
        if title in (None, ''):
            rep.append('Missing title')
            ok = False
        else:
            for k in create_database.key_table:
                if not k in film:
                    ok = False
                    rep.append("No %r in %s" % (k, title))
        if ok == True and create_database.insert_into(conn, cur, table, film):
            rep.append('OK')
        else:
            rep.append('Could not insert %s\n' % film.get('title',"'no title'"))
    conn.commit()
    conn.close()
    return HttpResponse("</br>".join(rep))

def display(request):
    conn = create_database.get_connection('localhost','formationdjango', 'djangouser', 'secret')
    if conn == None or not create_database.table_exist(conn, table):
        return HttpResponse("No data available")
    cur = conn.cursor()
    if cur == None:
        return HttpResponse("No data available")
    cur.execute(""" SELECT * FROM %s """ % table)
    try:
        data = cur.fetchall()
    except Exception as e:
        print (str(e))
        return HttpResponse("No data available")
    res = list()
    if data != None:
        res.append('<table style="border: .5px solid black"><tr>')
        for k in create_database.key_table:
            res.append('<th style="border: .5px solid black"> %s </th>' % k)
        res.append("</tr>")
        for d in data:
            res.append("<tr>")
            for c in d[1:]:
                if c != None:
                    res.append('<td style="border: .5px solid black"> %s </td>' % c)
            res.append("</tr>")
        res.append("</table>")
    else: 
        res.append("No data Available")
    conn.commit()
    conn.close()
    return HttpResponse("\n".join(res))