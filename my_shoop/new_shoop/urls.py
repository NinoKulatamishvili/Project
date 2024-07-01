from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('women/', views.about, name='women'),
    path('men/', views.about, name='men'),
    path('kids/', views.about, name='kids'),
    path('profile/<str:ms>', views.profile, name='profile')
]
