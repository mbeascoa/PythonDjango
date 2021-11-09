from django.urls import path

from gestion import views

urlpatterns=[
    path('',views.index,name='index'),
    path('futboll', views.equipo, name='equipo'),
    path('madrid', views.jugadores, name='jugadores'),
    path('amigos', views.amistades, name='amistades')
]
