from django.core.management import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        if get_user_model().objects.count() == 0:
            email = 'admin@email.com'
            password = 'password123'
            admin = get_user_model().objects.create_superuser(
                email=email, 
                password=password
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            print("Аккаунт администратора создан успешно")
        else:
            print("Аккаунт администратора был создан ранее")
