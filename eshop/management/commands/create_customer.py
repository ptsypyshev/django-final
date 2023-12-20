from django.core.management.base import BaseCommand, CommandParser
from eshop.models import Customer

class Command(BaseCommand):
    help = "Creates new customer"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Customer name')
        parser.add_argument('email', type=str, help='Customer email')
        parser.add_argument('phone', type=str, help='Customer phone')
        parser.add_argument('address', type=str, help='Customer address')

    def handle(self, *args, **kwargs):
        name, email, phone, address = kwargs['name'], kwargs['email'], kwargs['phone'], kwargs['address']
        customer = Customer(name=name, email=email, phone=phone, address=address)
        customer.save()
        self.stdout.write(f'{customer}')
