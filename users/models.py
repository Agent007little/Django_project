from django.db import models
from django.contrib.auth.models import User


class UserSubscription(models.Model):
    """Модель с подписками пользователя"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_followers_id')
    subscription_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_subscription_id')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'
