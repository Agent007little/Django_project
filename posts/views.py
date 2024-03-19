from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView


def home_page(request):
    """Функция выводит главную страницу"""
    return render(request, 'posts/home_page.html', {'title': 'ITwitter.com'})


class HomePage(ListView):
    model = User
    template_name = 'posts/home_page.html'
    context_object_name = 'users'

    def get_context_data(self, **kwards):
        ctx = super(HomePage, self).get_context_data(**kwards)

        ctx['title'] = 'Главная страница сайта'
        return ctx
