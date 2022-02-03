from django.urls import path
from . import views
# from .views import ShowProfilePageView, CreateProfilePageView

app_name = 'autontification'


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    # path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile')
]
