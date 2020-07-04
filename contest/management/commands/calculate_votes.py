from django.core.management import BaseCommand
from ._private import recalculate_votes


class Command(BaseCommand):
    help = 'Calculate song views count'

    def handle(self, *args, **options):
        recalculate_votes()
        self.stdout.write(self.style.SUCCESS("Successfully recalculated song votes"))
