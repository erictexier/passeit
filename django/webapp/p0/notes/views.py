from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from notes.models import Note


def home(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/home.html', context)

def about(request):
    return render(request, 'notes/about.html', {'title': 'About'})

class NoteListView(ListView):
    model = Note
    template_name = 'notes/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    ordering = ['-date_posted']
    paginate_by = 5


class UserNoteListView(ListView):
    model = Note
    template_name = 'notes/user_notes.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Note.objects.filter(author=user).order_by('-date_posted')


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NoteCreateView, self).form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NoteUpdateView, self).form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False
