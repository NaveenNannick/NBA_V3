from django.urls import path
from calc import views
from .views import export_data


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('avg/', views.Avg, name='avg'),
    path('export_data/', export_data, name='export_data'),
    
]
