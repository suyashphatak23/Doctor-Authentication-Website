from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Contact
from Services.models import Doctor


def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['message']

        print(phone)

        contact = Contact(fname=fname, lname=lname, email=email, phone=phone, message=msg)
        contact.save()
        messages.success(request, "Message Sent Successfully. We will be replying by mail.")
        return redirect('contact')

    else:
        return render(request, 'Contact.html')


def import_data(request):
    if 'term' in request.GET:
        qs = Doctor.objects.filter(name__istartswith=request.GET.get('term'))
        names = list()
        for doctor in qs:
            names.append(doctor.name)
        return JsonResponse(names, safe=False)
    return render(request, "Import.html")
