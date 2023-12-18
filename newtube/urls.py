"""
URL configuration for newtube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin 
from django.urls import include, path
from core import views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    path('upload/',views.upload, name='upload'),
    path('videoplayer<int:movie_id>/',views.videoplayer, name='videoplayer'),
    path('videoplayer/', views.videoplayer_without_id, name='videoplayer_without_id'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('theater/',views.theater, name='theater'),
    path('ticket/',views.ticket, name='ticket'),
    path('bookticket/',views.bookticket, name='bookticket'),
    path('theater/<int:theater_id>/', views.theaterdetails, name='theater_details'),
    path('logout/', views.logout, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('accounts/profile/', views.profile, name='profile'),








]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)