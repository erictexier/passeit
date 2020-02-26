from django.shortcuts import render, redirect
from django.http import HttpResponse
from ex03.models import Movies
# Same movie table than ex02_movies
from ex00 import create_database
from django.apps import apps

table = "ex02_movies"

def populate(request):
    rep = list()
    #create_database.do_it_make_table(table)
    list_film = create_database.DefaultTable(True)
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
        if ok == True:
            print (film.get('episode_nb'), film.get('title'))
            m = Movies( episode_nb= film.get('episode_nb'),
                        title=film.get('title'),
                        director=film.get('director'),
                        producer=film.get('producer'),
                        release_date=film.get('release_date'),
                        opening_crawl=film.get('opening_crawl',''))
            m.save()
            rep.append('OK')
        else:
            rep.append('Could not insert %s\n' % film.get('title',"'no title'"))
    return HttpResponse("</br>".join(rep))

def display(request):

    context = { 'movie_list': Movies.objects.order_by('release_date'), 
                'header_table': create_database.key_table + create_database.key_option,
                'title': 'STAR WARS legacy'}
    return render(request, "ex03/SWtable.html", context)

def delete_model(request):

    for m in  Movies.objects.all():
        m.delete()
    return redirect('ex03-display')