# Generated by Django 5.0.1 on 2024-03-06 06:43
from random import choice

from django.db import migrations


# Создание сообщений
def create_massages(apps, schema_editor):
    Massage = apps.get_model("posts", "Massage")
    User = apps.get_model("auth", "User")

    users = User.objects.all()[:10]  # Выбираем первых 10 пользователей

    massages_data = [
        {"text": "Прекрасный день для прогулки! 🌳", "author": users[0], "likes": choice(list(users))},
        {"text": "Уже скучаю за летом и морем... 🏖️", "author": users[1], "likes": choice(list(users))},
        {"text": "Завтра важное событие, нужно быть готовым! 💼", "author": users[2],
         "likes": choice(list(users))},
        {"text": "Сегодняшний фильм оставил глубокие впечатления! 🎬", "author": users[3],
         "likes": choice(list(users))},
        {"text": "Новый рецепт пирога просто божественный! 🍰", "author": users[4],
         "likes": choice(list(users))},
        {"text": "Хорошая книга - лучший спутник в долгой поездке! 📖", "author": users[5],
         "likes": choice(list(users))},
        {"text": "Праздничный ужин с семьей - лучший способ провести вечер! 🍽️", "author": users[6],
         "likes": choice(list(users))},
        {"text": "Встреча с давним другом была просто волшебной! ✨", "author": users[7],
         "likes": choice(list(users))},
        {"text": "Спортивная тренировка сегодня была особенно интенсивной! 💪", "author": users[8],
         "likes": choice(list(users))},
        {"text": "Новая игра завладела моим временем! 🎮", "author": users[9],
         "likes": choice(list(users))},
        # Добавляем еще 10 сообщений с параметром likes
        {"text": "Самое время для новых целей и достижений! 🎯", "author": users[0],
         "likes": choice(list(users))},
        {"text": "Вдохновение приходит в самые неожиданные моменты! ✨", "author": users[1],
         "likes": choice(list(users))},
        {"text": "Зимний вечер - отличное время для чтения книги у камина! 📚🔥", "author": users[2],
         "likes": choice(list(users))},
        {"text": "Мечты становятся реальностью, если верить в них настолько сильно, что не можешь не действовать! 💭💪",
         "author": users[3], "likes": choice(list(users))},
        {"text": "Лучший способ расслабиться после трудного дня - горячая ванна и любимая музыка! 🛁🎶",
         "author": users[4], "likes": choice(list(users))},
        {"text": "Новый рецепт ужина порадовал всех членов семьи! 🍲👨‍👩‍👧‍👦", "author": users[5],
         "likes": choice(list(users))},
        {"text": "Путешествие - это возможность увидеть мир шире и познакомиться с новыми культурами! 🌍✈️",
         "author": users[6], "likes": choice(list(users))},
        {"text": "Спорт - это не только физическое развитие, но и укрепление духа! 💪🧘‍♂️", "author": users[7],
         "likes": choice(list(users))},
        {"text": "Встреча со старыми друзьями всегда наполняет сердце радостью и теплотой! ❤️👫", "author": users[8],
         "likes": choice(list(users))},
        {"text": "Время проведенное с семьей - самое ценное время в жизни! 👨‍👩‍👧‍👦❤️", "author": users[9],
         "likes": choice(list(users))},
    ]

    for data in massages_data:
        Massage.objects.create(**data)


# Создание хэштегов
def create_hashtags(apps, schema_editor):
    Hashtag = apps.get_model("posts", "Hashtag")

    hashtags_data = [
        {"name": "#nature"},
        {"name": "#travel"},
        {"name": "#inspiration"},
        {"name": "#movies"},
        {"name": "#food"},
        {"name": "#books"},
        {"name": "#family"},
        {"name": "#friends"},
        {"name": "#fitness"},
        {"name": "#game"},
    ]

    for data in hashtags_data:
        Hashtag.objects.create(**data)


# Создаём связь хэштегов с сообщениями
def attach_hashtags_to_messages(apps, schema_editor):
    MassageHashtag = apps.get_model("posts", "MassageHashtag")
    Massage = apps.get_model("posts", "Massage")
    Hashtag = apps.get_model("posts", "Hashtag")

    messages = Massage.objects.all()[:10]
    hashtags = Hashtag.objects.all()

    for message in messages:
        hashtag = hashtags[0] # Берем первый хэштег для привязки к сообщению
        MassageHashtag.objects.create(massage_id=message, hashtag_id=hashtag)
        hashtags = hashtags[1:]  # Удаляем первый хэштег из списка


# Изображения
def attach_images_to_messages(apps, schema_editor):
    PostImage = apps.get_model("posts", "PostImage")
    Massage = apps.get_model("posts", "Massage")

    messages = Massage.objects.all()[:5]
    for message in messages:
        PostImage.objects.create(
            link='https://images.ctfassets.net/hrltx12pl8hq/6JHPcrEjyJWnAx8HY5eHWC/57d007fc85fa144bf5492c3651747e75/04-water_1777125524.jpg',
            massage_id=message)


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_massages),
        migrations.RunPython(create_hashtags),
        migrations.RunPython(attach_hashtags_to_messages),
        migrations.RunPython(attach_images_to_messages)
    ]
