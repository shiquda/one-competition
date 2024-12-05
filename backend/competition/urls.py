# backend/urls.py
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # 竞赛相关
    path('api/competitions/', views.get_all_competitions, name='get_all_competitions'),
    path('api/competition/<int:competition_id>/', views.get_competition_detail, name='get_competition_detail'),
    path('api/competition/add/', views.add_competition, name='add_competition'),
    path('api/competition/delete/<int:competition_id>/', views.delete_competition, name='delete_competition'),
    # 用户认证相关
    path('api/auth/register/', views.register, name='register'),
    path('api/auth/login/', views.login, name='login'),
    path('api/auth/change_password/', views.change_password, name='change_password'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
