from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', userViews.profile, name="profile"),
    path('login/', userViews.register, name="register"),
    path('auth/', userViews.LoginUser.as_view(), name="auth"),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name="exit"),
    path('', include('posts.urls'))
]

