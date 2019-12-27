from django.shortcuts import render
from .models import Feedback, Complaint


def index(request):
    feedback = Feedback.objects.all()
    complaints = Complaint.objects.all()
    return render(request, 'index.html',
                  {'feedback': feedback, 'complaints': complaints})


def searchbox(request):
    return render(request, 'searchbox.html')
