
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from ex00 import views as ex00_view
#from ex02 import views as ex02_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/init/', ex00_view.init, name='ex00-init'),
    path('ex02/', include('ex02.urls')),
    path('ex03/', include('ex03.urls'))
]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
