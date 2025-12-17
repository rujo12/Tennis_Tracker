from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('favourites/', views.favourites, name='favourites'),
    path('schedule/', views.schedule, name='schedule'),
    path('register/', views.register_view, name='register'),

    
]
