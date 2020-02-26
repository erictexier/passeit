from django.urls import path
from notes.views import NoteListView
from notes.views import NoteDetailView
from notes.views import NoteCreateView
from notes.views import NoteUpdateView
from notes.views import NoteDeleteView
from notes.views import UserNoteListView
from notes import views

urlpatterns = [
    path('', NoteListView.as_view(), name='notes-home'),
    path('about/', views.about, name='notes-about'),

    path('user/<str:username>', UserNoteListView.as_view(), name='user-notes'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete')
]