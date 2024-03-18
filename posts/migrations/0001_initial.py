# Generated by Django 5.0.1 on 2024-02-06 10:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название хэштега')),
            ],
        ),
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_massage', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_massage', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MassageHashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user_images.hashtag')),
                ('massage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_images.massage')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='URL изображения')),
                ('path', models.CharField(verbose_name='Путь до файла изображения')),
                ('massage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_images.massage')),
            ],
        ),
    ]
