from django.db import models
from django.contrib.auth.models import User


class UserSubscription(models.Model):
    """Модель с подписками пользователя"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_followers_id')
    subscription_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_subscription_id')
