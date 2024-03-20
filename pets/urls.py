from django.urls import path
from pets import views

app_name = 'pets'

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pets, name='pets'),
]