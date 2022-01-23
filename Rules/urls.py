from django.urls import path
from . import views

urlpatterns = [
    path('GovRules', views.GR, name='rules'),
    path('GovWebs', views.GW, name='websites'),
]
