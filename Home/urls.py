from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Feedback', views.feedback_form, name='feedback'),
    path('Complaint', views.complaint_form, name='complaint'),
]
