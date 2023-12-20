from django.core.management.base import BaseCommand, CommandParser
from eshop.models import Customer

class Command(BaseCommand):
    help = "Update a customer by ID"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='Customer ID')
        parser.add_argument('name', type=str, help='Customer name')

    def handle(self, *args, **kwargs):
        pk, name = kwargs['pk'], kwargs['name']
        customer = Customer.objects.filter(pk=pk).first()
        customer.name = name
        customer.save()
        self.stdout.write(f'{customer}')
