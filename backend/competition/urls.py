# backend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('competitions/', views.get_all_competitions, name='get_all_competitions'),
    path('competition/<int:competition_id>/', views.get_competition_detail, name='get_competition_detail'),
    path('competition/add/', views.add_competition, name='add_competition'),
    path('competition/delete/<int:competition_id>/', views.delete_competition, name='delete_competition'),
]
