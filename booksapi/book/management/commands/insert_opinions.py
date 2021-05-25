import pandas as pd
from django.core.management.base import BaseCommand, CommandError

from book.models import Book, Opinion


class Command(BaseCommand):
    help = "Inserts opinions from CSV file. "
    help += "Data format: ISBN;Ocena;Opis"

    def add_arguments(self, parser):
        parser.add_argument(
            "filename", type=str, help="Path to CSV file with opinions to insert."
        )

    def handle(self, *args, **options):
        filename = options["filename"]
        try:
            with open(filename, "r") as file:
                df = pd.read_csv(file, sep=";")
        except:
            raise CommandError(f"Could not read file {filename}.")

        for _, book in df.iterrows():
            opinion = Opinion(
                isbn=Book.objects.get(isbn=book["ISBN"]),
                rate=book["Ocena"],
                description=book["Opis"],
            )
            opinion.save()

        print(f"Successfully inserted {len(df)} opinions.")
