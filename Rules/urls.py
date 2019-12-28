from django.urls import path
from . import views

urlpatterns = [
    path('GovRules', views.GR, name='Government Rules'),
    path('GovWebs', views.GW, name='Government Websites'),
]
