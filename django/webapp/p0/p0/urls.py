from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from userprofile import views as userprofile_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', userprofile_views.register, name='register'),
    path('profile/', userprofile_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userprofile/logout.html'), name='logout'),
    
    #path('', include('psws.urls')),
    path('', include('notes.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
