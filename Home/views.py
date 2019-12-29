from django.shortcuts import render
from .models import Feedback, Complaint
from .forms import FeedbackForm, ComplaintForm


def index(request):
    feedback = Feedback.objects.all()
    complaints = Complaint.objects.all()
    return render(request, 'index.html',
                  {'feedback': feedback, 'complaints': complaints})


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "index.html", context)


def complaint(request):
    form = ComplaintForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)
