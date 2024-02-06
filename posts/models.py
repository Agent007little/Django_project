from django.db import models
from django.contrib.auth.models import User


class Massage(models.Model):
    """Модель сообщения пользователя"""
    text = models.TextField('Текст сообщения')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_massage')
    likes = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_massage')


class Hashtag(models.Model):
    """Модель с хэштегами сообщения"""
    name = models.CharField('Название хэштега')


class MassageHashtag(models.Model):
    """Связующая модель сообщений и хэштегов"""
    massage_id = models.ForeignKey(Massage, on_delete=models.CASCADE)
    hashtag_id = models.ForeignKey(Hashtag, on_delete=models.DO_NOTHING)


class PostImage(models.Model):
    """Модель изображений"""
    link = models.URLField('URL изображения')
    path = models.CharField('Путь до файла изображения')
    massage_id = models.ForeignKey(Massage, on_delete=models.CASCADE)
