from django.urls import path
from bson.objectid import ObjectId
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('recommend/', views.recommend, name='recommend'),
    path('watch/', views.watch, name='watch'),
    path('<str:movie_id>/', views.detail, name='detail'),
]