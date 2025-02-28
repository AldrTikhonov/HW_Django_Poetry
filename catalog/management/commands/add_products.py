from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Category.objects.all().delete()
        Product.objects.all().delete()
        # загружаем базу данных из фикстуры
        call_command('loaddata', 'catalog.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))