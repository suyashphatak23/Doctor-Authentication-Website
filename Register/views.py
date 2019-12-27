from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                            email=email, username=username,
                                            password=password1)
            user.save()
            messages.info(request, 'User created')
            return redirect('register')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')

    else:
        return render(request, 'NewAdmin.html')


def logout(request):
    auth.logout(request)
    return redirect('')
