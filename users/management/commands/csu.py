from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="tihas75@mail.ru")
        user.set_password("B987OMPolo+")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()