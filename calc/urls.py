from django.urls import path
from calc import views

urlpatterns = [
    path('calc/', views.dashboard, name='dashboard'),
]