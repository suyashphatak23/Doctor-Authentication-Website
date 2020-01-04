from django.urls import path
from . import views

urlpatterns = [
    path('Home', views.index, name='index'),
    path('Feedback', views.feedback_form, name='feedback'),
    path('Complaint', views.complaint_form, name='complaint'),
]
