from django.urls import path

from posts.views import home_page

urlpatterns = [
    path('', home_page)
]
