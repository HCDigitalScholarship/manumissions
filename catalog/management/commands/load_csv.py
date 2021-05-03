import csv
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count, Max

from catalog.models import * 

def remove_duplicate_people():
    unique_fields = ['first_name', 'last_name']

    duplicates = (
        Person.objects.values(*unique_fields)
        .order_by()
        .annotate(max_id=Max('id'), count_id=Count('id'))
        .filter(count_id__gt=1)
    )

    for duplicate in duplicates:
        (
            Person.objects
            .filter(**{x: duplicate[x] for x in unique_fields})
            .exclude(id=duplicate['max_id'])
            .delete()
        )

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=str)

    def handle(self, *args, **options):
        remove_duplicate_people()
        witnesses = ['Bailey, Ansolme',
        'Bailey, Joseph',
        'Butler, John',
        'Butler, Joseph',
        'Cornwell, John',
        'Fisher, David',
        'Hair, Henry',
        'Hopkins, Samuel',
        'Hunnicutt, John',
        'Hunnicutt, Robert',
        'Hunnicutt, Sarah',
        'Hunnicutt, Thomas',
        'Jones, Sam',
        'Peebles, Peter',
        'Pretlow, John',
        'Ricks, Thomas',
        'Russel, Benjamin',
        'Stabler, Edward',
        'Stabler, Mary',
        'Stanton, Samson']

        for witness in witnesses:
            first, last = witness.split(',')
            role, created = Role.objects.get_or_create(name='Witness')
            new_witness, created = Person.objects.get_or_create(
                first_name=first,
                last_name=last,
            )
            new_witness.role.add(role)

        reader = csv.DictReader(open(options['csv_path'][0]))  
        for row in reader:
            page_number, created = Page_Number.objects.get_or_create(page_number=row['Page Number'])

            image_name, created = Image_name.objects.get_or_create(image_name=row['Image Name (HC10-10002_XXX)'])

            date = row['Date (YYYY-MM-DD)'].split('-')
            date_of_manumission_signing = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))

            place_freed, created = Place_Freed.objects.get_or_create(place_freed=row['Place (Township, County, etc)'])
            # monthly_meeting ignore, no data this column
            # call_number, vestigial from Mozilla tutorial, I assume they mean image_name


            manumission, creates = Manumission.objects.get_or_create(
                title=row['Image Name (HC10-10002_XXX)'],
                date_of_manumission_signing=date_of_manumission_signing,
                image_name=image_name,
                page_number=page_number,
            )
            # Add enslaved people 
            for name, age_listed, freed_age, gender in zip(row['Name of Enslaved Person (Transcribe what is listed)'].split(','),row['Age listed for Enslaved Person'].split(','),row['Freed Age'].split(','),row['Gender of Enslaved Person'].split(',')):
                role, created = Role.objects.get_or_create(name='Enslaved Person')
                gender, created = Gender.objects.get_or_create(gender=gender)
                age_freed, created = Age_Freed.objects.get_or_create(age_freed=freed_age)
                age_listed, created = Age_Listed.objects.get_or_create(age_listed=age_listed)
                enslaved_person, created = Person.objects.get_or_create(
                    first_name=name,
                    gender=gender, 
                    age_freed=age_freed,
                    age_listed=age_listed,
                    year_manumitted=row['Date (YYYY-MM-DD)'],


                )
                enslaved_person.role.add(role)
                manumission.person.add(enslaved_person)
            # Add slaveholders people 
            first_name, last_name = row['Unabbreviated - Name of Slaveholder (Last name, First name)'].split(',')
            abbreviated_first_name, abbreviated_last_name = row['Transcribed - Name of Slaveholder (Last name, First name)'].split(',')
            gender, created = Gender.objects.get_or_create(gender=row['Gender of Slaveholder'])
            role, created = Role.objects.get_or_create(name='Slaveholder')
            slaveowner, created = Person.objects.get_or_create(
                first_name = first_name,
                last_name = last_name,
                abbreviated_first_name=abbreviated_first_name,
                abbreviated_last_name=abbreviated_last_name,
                gender=gender,
            )
            slaveowner.role.add(role)
            manumission.person.add(slaveowner)


            # Add witnesses 
            for witness in witnesses:
                if witness in row['Unabbreviated - Witnesses (ex: "Sealed and delivered in the Presence of...") (Last name, First name)']:
                    first, last = witness.split(',')
                    witness_person, created = Person.objects.get_or_create(first_name=first,last_name=last)  
                    manumission.person.add(witness_person)
            
        self.stdout.write(self.style.SUCCESS('Done'))
