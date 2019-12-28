from django.shortcuts import render


def GR(request):
    return render(request, 'GovernmentRules.html')


def GW(request):
    return render(request, 'GovernmentWebsites.html')
