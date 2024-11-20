# backend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/competitions/', views.get_all_competitions, name='get_all_competitions'),
    path('api/competition/<int:competition_id>/', views.get_competition_detail, name='get_competition_detail'),
    path('api/competition/add/', views.add_competition, name='add_competition'),
    path('api/competition/delete/<int:competition_id>/', views.delete_competition, name='delete_competition'),
]
