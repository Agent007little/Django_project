from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from users.models import UserSubscription, Profile

# python manage.py seed_user --mode=refresh

""" Clear all data and creates users """
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
    User.objects.exclude(id=User.objects.first().id).delete()
    UserSubscription.objects.all().delete()
    Profile.objects.all().delete()


def create_users():
    """Creates a user object that combines different elements from a list."""
    # logger.info("Creating Users in process...")
    users_data = [
        {"username": "Alex", "first_name": "Alex", "last_name": "Sean", "email": "alex@mail.com",
         "password": "Alex12345_"},
        {"username": "John", "first_name": "John", "last_name": "Doe", "email": "john.doe@mail.com",
         "password": "John12345_"},
        {"username": "Emily", "first_name": "Emily", "last_name": "Smith", "email": "emily.smith@mail.com",
         "password": "Emily12345_"},
        {"username": "Michael", "first_name": "Michael", "last_name": "Johnson", "email": "michael.johnson@mail.com",
         "password": "Michael12345_"},
        {"username": "Sarah", "first_name": "Sarah", "last_name": "Brown", "email": "sarah.brown@mail.com",
         "password": "Sarah12345_"},
        {"username": "David", "first_name": "David", "last_name": "Wilson", "email": "david.wilson@mail.com",
         "password": "David12345_"},
        {"username": "Emma", "first_name": "Emma", "last_name": "Davis", "email": "emma.davis@mail.com",
         "password": "Emma12345_"},
        {"username": "James", "first_name": "James", "last_name": "Martinez", "email": "james.martinez@mail.com",
         "password": "James12345_"},
        {"username": "Olivia", "first_name": "Olivia", "last_name": "Garcia", "email": "olivia.garcia@mail.com",
         "password": "Olivia12345_"},
        {"username": "Daniel", "first_name": "Daniel", "last_name": "Rodriguez", "email": "daniel.rodriguez@mail.com",
         "password": "Daniel12345_"},
    ]

    for user_data in users_data:
        User.objects.create(**user_data)

    create_user_subscription()
    create_profile()
    # logger.info("Creating Users completed")


def create_user_subscription():
    users = User.objects.all()

    # Создаем связи между пользователями
    for user in users:
        # Пример: создаем подписку пользователя John на пользователя Emily
        if user.username == "John":
            subscription_user1 = User.objects.get(username="Emily")
            subscription_user2 = User.objects.get(username="Sarah")
            subscription_user3 = User.objects.get(username="Alex")
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user1)
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user2)
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user3)

        # Продолжаем добавлять связи между другими пользователями по аналогии
        elif user.username == "Emily":
            subscription_user1 = User.objects.get(username="John")
            subscription_user2 = User.objects.get(username="Sarah")
            subscription_user3 = User.objects.get(username="Alex")
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user1)
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user2)
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user3)

        elif user.username == "Sarah":
            subscription_user1 = User.objects.get(username="John")
            subscription_user2 = User.objects.get(username="Emily")
            subscription_user3 = User.objects.get(username="Alex")
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user1)
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user2)
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user3)

        elif user.username == "Alex":
            subscription_user1 = User.objects.get(username="John")
            subscription_user2 = User.objects.get(username="Emily")
            subscription_user3 = User.objects.get(username="Sarah")
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user1)
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user2)
            UserSubscription.objects.create(user_id=user, subscription_id=subscription_user3)


def create_profile():
    users = User.objects.all()[1:]

    for num, user in enumerate(users, start=1):
        img = 'image_' + str(num) # здесь должно быть заполнение аватарок.
        Profile.objects.create(user=user)


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating users
    create_users()
