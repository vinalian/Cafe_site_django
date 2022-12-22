from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def registration(request):
    data = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Всё прошло успешно"
            return render(request, 'registration/registration.html', data)
    else:
        form = UserCreationForm()
        data['form'] = form
        return render(request, 'registration/registration.html', data)


def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})


