from django.core.management.base import BaseCommand, CommandParser
from eshop.models import Customer

class Command(BaseCommand):
    help = "Read a customer by ID"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        customer = Customer.objects.filter(pk=pk).first()
        self.stdout.write(f'{customer}')
