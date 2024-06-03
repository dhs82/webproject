from django.urls import path

from . import views


urlpatterns = [
    path('', views.homelands, name='homelands'),
    path('info/', views.info, name='info'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('recommend/', views.recommend, name='recommend'),
    path('test/', views.recommend, name='test')
]
