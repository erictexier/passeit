from django.urls import path

from psws.views import MoviesListView
from psws.views import MoviesDetailView
from psws.views import MoviesCreateView
from psws.views import MoviesUpdateView
from psws.views import MoviesDeleteView
#from notes.views import UserMovieListView

from psws import views

urlpatterns  = [
    path('populate', views.populate, name='psws-populate'),

    path('', MoviesListView.as_view(), name='psws-home'),
    path('about/', views.about, name='psws-about'),

    #path('user/<str:username>', UserNoteListView.as_view(), name='pswsuser-notes'),
    path('psws/<int:pk>/', MoviesDetailView.as_view(), name='psws-detail'),
    path('psws/new', MoviesCreateView.as_view(), name ='psws-create'),
    path('psws/<int:pk>/update/', MoviesUpdateView.as_view(), name='psws-update'),
    path('psws/<int:pk>/delete/', MoviesDeleteView.as_view(), name='psws-delete'),
]

