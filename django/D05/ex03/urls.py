from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns  = [
    path('populate', views.populate, name='ex03-populate'),
    path('display', views.display, name ='ex03-display'),
    path('delete_model', views.delete_model, name='ex03-delete')
]

