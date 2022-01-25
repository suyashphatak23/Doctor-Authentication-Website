from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


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
