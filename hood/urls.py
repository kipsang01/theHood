from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('home', views.home, name='home'),
  path('<neighbourhood>/post', views.post, name='post'),  
  path('new-hood', views.new_hood, name='new-hood'),  
  path('join/<hood_id>', views.join_hood, name='join'),  
]
