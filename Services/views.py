from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Doctor
from Home.models import Feedback, Complaint
from datetime import datetime


def SearchDoctor(request):
    doctors = Doctor.objects.all()

    if request.method == 'GET':
        query = request.GET.get('search')
        if 'term' in request.GET:
            qs = Doctor.objects.filter(name__istartswith=request.GET.get('term'))
            names = list()
            for doctor in qs:
                names.append(doctor.name)
            return JsonResponse(names, safe=False)
        if query:
            result = Doctor.objects.filter(Q(name__icontains=query) |
                                           Q(location__icontains=query))
            if result:
                count = len(result)
                doctor_paginator = Paginator(doctors, 10)
                page_num = request.GET.get('page')
                page = doctor_paginator.get_page(page_num)
                context = {
                    'sr': result,
                    'count': count,
                    'page': page,
                    'query': query,
                    'doctors': doctors,
                }
                return render(request, 'SearchDoc.html', context)
            else:
                context = {
                    'query': query,
                    'doctors': doctors,
                    'page': page,
                }
                messages.error(request, 'Search Not Found in Records')
                return render(request, 'SearchDoc.html', context)
        else:
            return redirect('SearchPage')


def SearchPage(request):
    doctors = Doctor.objects.all()
    if len(doctors) < 10:
        context = {
            'doctors': doctors,
        }
        return render(request, 'SearchDoc.html', context)
    else:
        doctor_paginator = Paginator(doctors, 10)
        page_num = request.GET.get('page')
        page = doctor_paginator.get_page(page_num)

        if 'term' in request.GET:
            qs = Doctor.objects.filter(name__istartswith=request.GET.get('term'))
            names = list()
            for doctor in qs:
                names.append(doctor.name)
            return JsonResponse(names, safe=False)
        context = {
            'doctors': doctors,
            'page': page,
        }
        return render(request, 'SearchDoc.html', context)


def Detail_view(request, doctor_id):
    if request.method == 'POST':
        if request.POST.get('feedback'):
            text = request.POST['feedback_text']
            feedback = Feedback.objects.create(doctor_id=doctor_id, feedback=text, datetime=datetime.now())
            feedback.save()
            return redirect('SearchPage')

        if request.POST.get('complaint'):
            text = request.POST['complaint_text']
            complaint = Complaint.objects.create(doctor_id=doctor_id, complaint=text, datetime=datetime.now())
            complaint.save()
            return redirect('SearchPage')

    feedbacks = Feedback.objects.filter(doctor_id=doctor_id)
    complaints = Complaint.objects.filter(doctor_id=doctor_id)
    context = {
        'doctor': Doctor.objects.get(registration_number=doctor_id),
        'feedbacks': feedbacks,
        'complaints': complaints,
    }
    return render(request, 'detail.html', context)
