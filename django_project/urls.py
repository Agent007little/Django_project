from django.contrib import admin
from django.urls import path, include
from users import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('profile/', userViews.profile, name="profile"),
    path('login/', userViews.register, name="register")
]

