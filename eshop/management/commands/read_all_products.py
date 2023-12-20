from django.core.management.base import BaseCommand
from eshop.models import Product

class Command(BaseCommand):
    help = "Reads all products"

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        self.stdout.write(f'{products}')
