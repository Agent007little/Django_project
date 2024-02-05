from django.shortcuts import render, HttpResponse


def hello_world(request):
    """Функция выводит фразу hello world на главной странице"""
    return HttpResponse('hello world')
