from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchDoctor, name='home_search'),
    path('searchpage/', views.SearchPage, name="SearchPage"),
    path('search_doctor/', views.SearchDoctor, name='SearchDoctor'),
    path('doctor/<int:doctor_id>/', views.Detail_view, name='detailed_view'),
]
