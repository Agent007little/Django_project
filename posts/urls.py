from django.urls import path

from posts.views import hello_world

urlpatterns = [
    path('', hello_world)
]
