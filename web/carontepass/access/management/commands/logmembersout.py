from access.models import Log
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):

    help = 'Logs all currently logged in users out.'

    def handle(self, *args, **options):

        Log.objects.filter(user_in=True).update(user_in=False, ts_output=timezone.now())