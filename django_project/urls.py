from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # добавляем путь к приложению posts
    path('profile/', include('users.urls'))
]

