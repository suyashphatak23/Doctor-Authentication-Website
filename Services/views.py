from django.db.models import Q
from .models import Doctor
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse


def SearchDoctor(request):
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
                paginator = Paginator(result, 1)
                page = request.GET.get('page')
                result = paginator.get_page(page)
                page = 2
                context = {
                    'sr': result,
                    'count': count,
                    'page': page,
                    'query': query,
                }
                return render(request, 'SearchDoc.html', context)
            else:
                context = {
                    'query': query,
                }
                messages.error(request, 'Search Not Found in Records')
                return render(request, 'SearchDoc.html', context)
        else:
            return redirect('SearchPage')


def SearchPage(request):
    if 'term' in request.GET:
        qs = Doctor.objects.filter(name__istartswith=request.GET.get('term'))
        names = list()
        for doctor in qs:
            names.append(doctor.name)
        return JsonResponse(names, safe=False)
    return render(request, 'SearchDoc.html')


def Detail_view(request, doctor_id):
    context = {
        'doctor': Doctor.objects.get(registration_number=doctor_id),
    }
    return render(request, 'detail.html', context)
