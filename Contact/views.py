from django.shortcuts import render
from .forms import ContactForm, SuperAdminForm
from django.contrib import messages


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid:
        form.save()
        if form.save():
            messages.info(request, 'Submitted Successfully')
        else:
            messages.info(request, 'Not Submitted Please Try Again')

    context = {
        'form': form
    }

    return render(request, 'Contact.html', context)


def admin(request):
    form = SuperAdminForm(request.POST or None)
    if form.is_valid:
        form.save()

    context = {
        'form': form
    }

    return render(request, 'Contact.html', context)
