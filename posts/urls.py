from django.urls import path

from posts.views import home_page, HomePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage.as_view(), name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
