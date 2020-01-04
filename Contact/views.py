from django.shortcuts import render
from .forms import ContactForm, SuperAdminForm
from django.contrib import messages


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        result = form.save()
        result.save()
        messages.info(request, "Saved Successfully")
        return render(request, 'Contact.html')

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
            return render(request, 'adminrequest.html', {'result': result})

    else:
        form = SuperAdminForm()

    context = {
        'form': form
    }

    return render(request, 'adminrequest.html', context)
