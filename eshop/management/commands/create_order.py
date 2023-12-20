from django.core.management.base import BaseCommand, CommandParser
from eshop.models import Customer, Order, Product

class Command(BaseCommand):
    help = "Creates new order"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('customer_id', type=int, help='Customer ID')
        parser.add_argument('product_id', type=int, help='Product ID')
        parser.add_argument('total_price', type=float, help='Total Price')

    def handle(self, *args, **kwargs):
        customer_id, product_id, total_price = kwargs['customer_id'], kwargs['product_id'], kwargs['total_price']
        customer = Customer.objects.filter(pk=customer_id).first()
        if not customer:
            self.stdout.write(f'bad customer id: {customer_id}')
            return

        product = Product.objects.filter(pk=product_id).first()
        if not product:
            self.stdout.write(f'bad product id: {product_id}')
            return

        order = Order(customer=customer, total_price=total_price)
        order.save()
        order.product.add(product)
        self.stdout.write(f'{order}')