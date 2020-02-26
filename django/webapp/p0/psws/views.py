from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.apps import apps
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from psws.models import Movies
# Same movie table than Starwars
from psws import create_database

def home(request):
    context = {
        'notes': Movies.objects.all()
    }
    return render(request, 'psws/home.html', context)


def about(request):
    return render(request, 'psws/about.html', {'title': 'About'})

def populate(request):
    rep = list()
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
    return render(request, "psws/SWtable.html", context)

def delete_model(request):

    for m in  Movies.objects.all():
        m.delete()
    return redirect('psws-home')

class MoviesListView(ListView):
    model = Movies
    template_name = 'psws/SWtable.html'
    context_object_name = 'movie_list'
    ordering = 'release_date'

class MoviesDetailView(DetailView):
    model = Movies

class MoviesCreateView(CreateView):
    model = Movies
    fields = ['title','director','producer','release_date','opening_crawl']

    def form_valid(self, form):
        #form.instance.author = self.request.user
        return super().form_valid(form)


class MoviesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movies
    fields = ['title', 'content']

    def form_valid(self, form):
        #form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if 0: #self.request.user == post.author:
            return True
        return False


class MoviesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movies
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

