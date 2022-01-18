from django.shortcuts import render
from .forms import ContactForm
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
