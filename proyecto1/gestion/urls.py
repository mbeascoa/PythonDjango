from django.urls import path

from gestion import views

urlpatterns=[
    path('',views.index,name='index')
 #   path('a',views.alta,name='index')
 #   path('b',views.baja,name='index')
]
