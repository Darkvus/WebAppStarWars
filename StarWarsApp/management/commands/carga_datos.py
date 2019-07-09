from django.core.management.base import BaseCommand, CommandError
import logging

from StarWarsApp.services.load_data import LoadData


class Command(BaseCommand):
    help = 'Load data api in database'

    def handle(self, *args, **kwargs):
        try:
            LoadData.execute()
        except Exception as e:
            logging.exception(e)
