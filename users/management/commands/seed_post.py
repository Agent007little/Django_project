from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from random import choice

from posts.models import Massage, Hashtag, MassageHashtag, PostImage

# python manage.py seed_user --mode=refresh

""" Clear all data and creates posts """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all table data except admin."""
    # logger.info("Delete User instances")
    Massage.objects.all().delete()
    Hashtag.objects.all().delete()
    MassageHashtag.objects.all().delete()
    PostImage.objects.all().delete()
    attach_images_to_messages()


def create_posts():
    """Creates posts"""
    # logger.info("Creating Users in process...")
    create_massages()
    create_hashtags()
    attach_hashtags_to_messages()
    attach_images_to_messages()
    # logger.info("Creating Users completed")


def create_massages():
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


def create_hashtags():
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
def attach_hashtags_to_messages():
    messages = Massage.objects.all()[:10]
    hashtags = Hashtag.objects.all()

    for message in messages:
        hashtag = hashtags[0]  # Берем первый хэштег для привязки к сообщению
        MassageHashtag.objects.create(massage_id=message, hashtag_id=hashtag)
        hashtags = hashtags[1:]  # Удаляем первый хэштег из списка


# Изображения
def attach_images_to_messages():
    messages = Massage.objects.all()[:5]
    for message in messages:
        PostImage.objects.create(
            link='https://images.ctfassets.net/hrltx12pl8hq/6JHPcrEjyJWnAx8HY5eHWC/57d007fc85fa144bf5492c3651747e75/04-water_1777125524.jpg',
            massage_id=message)


def run_seed(self, mode):
    """ Seed database based on mode
    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating posts
    create_posts()
