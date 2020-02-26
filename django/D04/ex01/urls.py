from django.conf import settings
#from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns  = [
    path('django', views.index, name='ex01-django'),
    path('affichage', views.affichage, name='ex01-affichage'),
    path('templates', views.template_engine, name='ex01-template')
]

#if settings.DEBUG:
#    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
