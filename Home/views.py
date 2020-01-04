from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Feedback, Complaint
from .forms import FeedbackForm, ComplaintForm


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
            messages.info(request, 'Feedback Submitted Successfully')
            return render(request, 'feedback.html', )
    else:
        form = FeedbackForm()

    feedback = Feedback.objects.all()
    return render(request, 'feedback.html',
                  {'form': form, 'feedback': feedback})


def complaint_form(request):
    form = ComplaintForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.info(request, 'Complaint Submitted Successfully')

    complaint = Complaint.objects.all()
    context = {
        'form': form,
        'complaints': complaint,
    }
    return render(request, 'complaint.html', context)


def index(request):
    return render(request, 'index.html')
