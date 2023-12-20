from django.core.management.base import BaseCommand, CommandParser
from eshop.models import Order

class Command(BaseCommand):
    help = "Read a order by ID"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')
