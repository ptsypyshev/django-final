from django.core.management.base import BaseCommand, CommandParser
from eshop.models import Order, Product

class Command(BaseCommand):
    help = "Update an order by ID"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('product_id', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk, product_id = kwargs['pk'], kwargs['product_id']
        order = Order.objects.filter(pk=pk).first()
        product = Product.objects.filter(pk=product_id).first()
        order.product.add(product)
        order.save()
        self.stdout.write(f'{order}')
