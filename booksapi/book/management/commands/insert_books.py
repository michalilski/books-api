from django.core.management.base import BaseCommand, CommandError
from book.models import Book
import pandas as pd

class Command(BaseCommand):
    help = 'Inserts book from CSV file. '
    help += 'Data format: ISBN;Tytuł;Autor;Gatunek'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Path to CSV file with books to insert.')

    def handle(self, *args, **options):
        filename = options['filename']
        try:
            with open(filename, 'r') as file:
                df = pd.read_csv(file, sep=';')
        except:
            raise CommandError(f'Could not read file {filename}.')
        
        
        successfully_created = 0
        for _, book in df.iterrows():
            _, success = Book.objects.get_or_create(
                isbn = book['ISBN'],
                title = book['Tytuł'],
                author = book['Autor'],
                genre = book['Gatunek'],
            )
        if success:
            successfully_created += 1

        print(f'Successfully inserted {successfully_created}/{len(df)} books.')