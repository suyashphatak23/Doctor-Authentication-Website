from django.urls import path
from . import views

urlpatterns = [
    path('SearchDoctor', views.SearchDoctor, name='SearchDoctor'),
    path('results', views.Search, name='search'),
]