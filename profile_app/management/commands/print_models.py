from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    def handle(self, *args, **options):
        models = apps.get_models()
        print('Models created -', len(models))
        for model in models:
            print("Model Name - {} (Objects created - {})".format(model.__name__, len(model.objects.all())))
