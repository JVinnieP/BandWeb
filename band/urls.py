from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('home.html', views.home, name="index"),
	path('juan.html', views.juan, name="juan"),
]