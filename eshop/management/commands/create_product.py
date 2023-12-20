from django.core.management.base import BaseCommand, CommandParser
from eshop.models import Product

class Command(BaseCommand):
    help = "Creates new product"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('qty', type=int, help='Product qty')

    def handle(self, *args, **kwargs):
        name, description, price, qty = kwargs['name'], kwargs['description'], kwargs['price'], kwargs['qty']
        product = Product(name=name, description=description, price=price, qty=qty)
        product.save()
        self.stdout.write(f'{product}')
