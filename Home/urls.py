from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('feedback', views.feedback, name="feedback"),
    path('complaint', views.complaint, name="complaint"),
]
