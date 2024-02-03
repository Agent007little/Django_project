from django.shortcuts import render


def home_page(request):
    """Функция выводит главную страницу"""
    return render(request, 'posts/home_page.html', {'title': 'ITwitter.com'})
