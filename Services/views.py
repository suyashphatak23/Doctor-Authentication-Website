from django.db.models import Q
from .models import Doctor
from django.shortcuts import render, redirect
from django.contrib import messages


def SearchDoctor(request):
    return render(request, 'SearchDoc.html')


def Search(request):
    if request.method == 'GET':
        query = request.GET.get('search')

        if query:
            result = Doctor.objects.filter(Q(name__icontains=query) |
                                           Q(location__icontains=query))

            if result:
                count = len(result)
                return render(request, 'SearchDoc.html', {'sr': result, 'count': count},)
            else:
                messages.error(request, 'Search Not Found in Records')
        else:
            return redirect('SearchDoctor')
    return render(request, 'SearchDoc.html')
