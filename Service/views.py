from django.db.models import Q
from .models import Doctor
from django.shortcuts import render, redirect
from django.contrib import messages


def SearchDoctor(request):
    count = Doctor.objects.all().count()
    context = {
        'count': count
    }
    return render(request, 'SearchDoc.html', context)


def Search(request):
    count = Doctor.objects.all().count()
    context = {
        'count': count
    }
    if request.method == 'GET':
        query = request.GET.get('search')

        if query:
            result = Doctor.objects.filter(Q(name__icontains=query) |
                                           Q(location__icontains=query))

            if result:
                return render(request, 'SearchDoc.html', {'sr': result}, context)
            else:
                messages.error(request, 'Search Not Found in Records')
        else:
            return redirect('SearchDoctor', context)

    return render(request, 'SearchDoc.html', context)
