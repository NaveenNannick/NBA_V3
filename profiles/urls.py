from django.urls import path
from profiles import views
from django.urls import path
from .views import PublicationListView, PublicationCreateView, PublicationUpdateView, PublicationDeleteView, publication_detail

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
   path('list/', PublicationListView.as_view(), name='publication_list'),
    path('<int:pk>/add/', PublicationCreateView.as_view(), name='publication_create'),
    path('<int:pk>/', publication_detail, name='publication_detail'),
    path('<int:pk>/update/', PublicationUpdateView.as_view(), name='publication_update'),
    path('<int:pk>/delete/', PublicationDeleteView.as_view(), name='publication_delete'),
]
