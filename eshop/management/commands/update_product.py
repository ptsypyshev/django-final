from django.core.management.base import BaseCommand, CommandParser
from eshop.models import Product

class Command(BaseCommand):
    help = "Update a customer by ID"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('qty', type=int, help='Product qty')

    def handle(self, *args, **kwargs):
        pk, name, price, qty = kwargs['pk'], kwargs['name'], kwargs['price'], kwargs['qty']
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.price = price
        product.qty = qty
        product.save()
        self.stdout.write(f'{product}')
