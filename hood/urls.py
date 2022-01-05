from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('home', views.home, name='home'),
  path('home/post/<post_id>', views.post, name='post'),  
  path('new-hood', views.new_hood, name='new-hood'),
  path('home/new-post', views.create_post, name='new-post'),   
  path('join/<hood_id>', views.join_hood, name='join'), 
  path('leave-hood', views.leave_hood, name='leave'),
  path('business', views.business, name='business'),  
  path('schools', views.school, name='schools'), 
  path('hospitals', views.hospital, name='hospitals'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

