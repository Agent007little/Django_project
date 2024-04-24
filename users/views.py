from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginUserForm
from django.contrib import messages


def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользовать {username} был успешно создан!')
            return redirect('profile')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Страница регистрации',
            'form': form
        }
    )


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/auth.html"
    extra_context = {"title": "Авторизация"}