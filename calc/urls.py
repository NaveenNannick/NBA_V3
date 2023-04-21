from django.urls import path
from calc import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('avg/', views.Avg, name='avg'),
    
]
