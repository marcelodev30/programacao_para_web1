from django.urls import include, path
from . import views

urlpatterns = [
    path('pesquisar',views.pesquisar,name='pesquisar'),
    path('home',views.home,name='home')
]
