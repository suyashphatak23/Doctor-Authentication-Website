from django.shortcuts import render


def SearchDoctor(request):
    return render(request, 'SearchDoc.html')
