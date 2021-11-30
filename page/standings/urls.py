from django.urls import path
from . import views

urlpatterns = (
    path('personal_standing/', views.personal_standing, name='personal_standing'),
    path('team_standing/', views.team_standing, name='team_standing'),
)
