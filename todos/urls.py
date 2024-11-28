from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('complete/<int:pk>/', views.complete_todo, name='complete_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('edit/<int:pk>/', views.edit_todo, name='edit_todo'),
]
