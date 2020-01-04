from django.shortcuts import render, redirect
from .forms import ContactForm, SuperAdminForm
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            result = form.save()
            messages.info(request, "Saved Successfully")
            return redirect(request, 'Contact.html', {'result': result})

    else:
        form = ContactForm()

    context = {
        'form': form



        
    }

    return render(request, 'Contact.html', context)


def admin(request):
    if request.method == 'POST':
        form = SuperAdminForm(request.POST)
        if form.is_valid():
            result = form.save()
            messages.info(request, "Saved Successfully")
            return redirect(request, 'Contact.html', {'result': result})

    else:
        form = SuperAdminForm()

    context = {
        'form': form
    }

    return render(request, 'Contact.html', context)
