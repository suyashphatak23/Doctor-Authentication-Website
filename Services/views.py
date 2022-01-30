from django.db.models import Q
from .models import Doctor
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse


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
    context = {
        'doctor': Doctor.objects.get(registration_number=doctor_id),
    }
    return render(request, 'detail.html', context)
