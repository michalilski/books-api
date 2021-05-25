import pandas as pd
from django.core.management.base import BaseCommand, CommandError

from book.models import Book, Opinion


class Command(BaseCommand):
    """Command class for opinion insertion.

    This command lets user to insert opinion to database
    using CSV file.
    """
    help = "Inserts opinions from CSV file. "
    help += "Data format: ISBN;Ocena;Opis"

    def add_arguments(self, parser):
        parser.add_argument(
            "filename", type=str, help="Path to CSV file with opinions to insert."
        )

    def handle(self, *args, **options):
        #filename if path to file passed by argument "filename" added in add_arguments method
        filename = options["filename"]
        try:
            with open(filename, "r") as file:
                #creating data frame using pandas
                df = pd.read_csv(file, sep=";")
        except:
            raise CommandError(f"Could not read file {filename}.")

        for _, opinion in df.iterrows():
            #getting book with current opinion if exists
            try:
                book = Book.objects.get(isbn=opinion["ISBN"])
            except:
                raise Book.DoesNotExist()

            opinion = Opinion(
                isbn=book,
                rate=opinion["Ocena"],
                description=opinion["Opis"],
            )
            opinion.save()

        print(f"Successfully inserted {len(df)} opinions.")
