from django.db.models import Q
from .models import Doctor
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
                paginator = Paginator(result, 1)
                page = request.GET.get('page')
                result = paginator.get_page(page)
                page = 2
                return render(request, 'SearchDoc.html', {'sr': result, 'count': count, page: 'page'})
            else:
                messages.error(request, 'Search Not Found in Records')
        else:
            return redirect('SearchDoctor')

    return render(request, 'SearchDoc.html')


def Detail_view(request, doctor_id):
    context = {
        'doctor': Doctor.objects.get(id=doctor_id),
    }
    return render(request, 'detail.html', context)
