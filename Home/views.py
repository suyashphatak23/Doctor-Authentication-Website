from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Feedback, Complaint

def index(request):
    return render(request, 'index.html')

def feedback(request):
    if request.method == "POST":
        doctor_id = request.POST['doctor_id']
        feedback_txt = request.POST['feedback_text']
        date_time = datetime.now()

        try:
            doctor_id = int(doctor_id)
            feedback_o = Feedback.objects.create(doctor_id=doctor_id, feedback=feedback_txt, datetime=date_time)
            feedback_o.save()
            return redirect('home')

        except Exception as e:
            print(e)
            return redirect('feedback')
    return render(request, 'feedback.html')


def complaint(request):
    if request.method == "POST":
        doctor_id = request.POST['doctor_id']
        complaint_text = request.POST['complaint_text']
        date_time = datetime.now()

        try:
            doctor_id = int(doctor_id)
            complaint_o = Complaint.objects.create(doctor_id=doctor_id, complaint=complaint_text, datetime=date_time)
            complaint_o.save()
            return redirect('home')

        except Exception as e:
            print(e)
            return redirect('complaint')
    return render(request, 'complaint.html')