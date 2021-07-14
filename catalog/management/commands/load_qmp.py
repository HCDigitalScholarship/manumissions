import csv
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count, Max

from catalog.models import * 
from django.core.exceptions import MultipleObjectsReturned

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
# issues, name of manumission is currently filename, needs to be other format 

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=str)

    def handle(self, *args, **options):
    
        reader = csv.DictReader(open(options['csv_path'][0]))  
        for row in reader:

            witnesses = []
            for witness in row['Unabbreviated - Witnesses (ex: "Sealed and delivered in the Presence of...") (Last name, First name)'].split(';'):
                if witness not in witnesses:
                    witnesses.append(witness)

            page_number, created = Page_Number.objects.get_or_create(page_number=row['Page Number'])
            if len(row['Image Name (HC10-10002_XXX)'].split(','))> 1:
                for image in row['Image Name (HC10-10002_XXX)'].split(','):
                    image_name, created = Image_name.objects.get_or_create(image_name=image)
            else:
                image_name, created = Image_name.objects.get_or_create(image_name=row['Image Name (HC10-10002_XXX)'])

            date = row['Date (YYYY-MM-DD)'].split('-')
            if len(date) != 3:
                date = False

            place_freed, created = Place_Freed.objects.get_or_create(place_freed=row['Place (Township, County, etc)'])
            # # monthly_meeting ignore, no data this column

            monthly_meeting, created = Monthly_Meeting.objects.get_or_create(monthly_meeting=row['Monthly Meeting'])
            print(monthly_meeting)
            # # call_number, vestigial from Mozilla tutorial, I assume they mean image_name

            manu_title = 'Manumission of ' + row['Name of Enslaved Person (Transcribe what is listed)'] + ', ' + row['Date (YYYY-MM-DD)']

            manumission, created = Manumission.objects.get_or_create(
                title= manu_title,
                image_name=image_name,
                page_number=page_number,
            )
            manumission.monthly_meeting = monthly_meeting
            manumission.save()

            if date:
                date_of_manumission_signing = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
                manumission.date_of_manumission_signing=date_of_manumission_signing,
            # # Add enslaved people 
            for name, age_listed, freed_age, gender in zip(row['Name of Enslaved Person (Transcribe what is listed)'].split(','),row['Age listed for Enslaved Person'].split(','),row['Freed Age'].split(','),row['Assumed Gender of Enslaved Person'].split(',')):
                role, created = Role.objects.get_or_create(name='Enslaved Person')
                gender, created = Gender.objects.get_or_create(gender=gender)
                age_freed, created = Age_Freed.objects.get_or_create(age_freed=freed_age)
                age_listed, created = Age_Listed.objects.get_or_create(age_listed=age_listed)
                try:
                    enslaved_person, created = Person.objects.get_or_create(
                        first_name=name,
                        gender=gender, 
                        age_freed=age_freed,
                        age_listed=age_listed,
                        year_manumitted=row['Date (YYYY-MM-DD)'],
                    )
                    enslaved_person.role.add(role)
                    manumission.person.add(enslaved_person)
                except MultipleObjectsReturned:
                    remove_duplicate_people()

                
            # Add slaveholders people 
            if len(row['Unabbreviated - Name of Slaveholder (Last name, First name)'].split(';')) > 1:
                
                for full_name, abbreviate_name, gender in zip(row['Unabbreviated - Name of Slaveholder (Last name, First name)'].split(';'), row['Transcribed - Name of Slaveholder (Last name, First name)'].split(';'),row['Gender of Slaveholder'].split(',')):
                    #print('108',full_name.split(','))
                    first_name, last_name = full_name.split(',')
                    if len(abbreviate_name.split(',')) > 1:
                        abbreviated_first_name, abbreviated_last_name = abbreviate_name.split(',')
                    else:
                        abbreviated_first_name, abbreviated_last_name = '',''
                    gender, created = Gender.objects.get_or_create(gender=gender)
                    role, created = Role.objects.get_or_create(name='Slaveholder')
                    slaveowner, created = Person.objects.get_or_create(
                        first_name = first_name,
                        last_name = last_name,
                        abbreviated_first_name=abbreviated_first_name.strip(),
                        abbreviated_last_name=abbreviated_last_name.strip(),
                        gender=gender,
                    )
                    slaveowner.role.add(role)
                    manumission.person.add(slaveowner)
            else:
                #print('[*] 130',row['Unabbreviated - Name of Slaveholder (Last name, First name)'].split(','))
                if len(row['Unabbreviated - Name of Slaveholder (Last name, First name)'].split(',')) > 1:
                    first_name, last_name = row['Unabbreviated - Name of Slaveholder (Last name, First name)'].split(',')
                else: 
                    first_name, last_name = '',''
                if len(row['Transcribed - Name of Slaveholder (Last name, First name)'].split(',')) > 1:
                    abbreviated_first_name, abbreviated_last_name = row['Transcribed - Name of Slaveholder (Last name, First name)'].split(',')
                else:
                    abbreviated_first_name, abbreviated_last_name = '',''
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
         #   for witness in row['Unabbreviated - Witnesses (ex: "Sealed and delivered in the Presence of...") (Last name, First name)'].split(';'):
          #      if len(witness.split(',')) >1:
                    #print('[*] 131',witness.split(','))
           #         first, last = witness.split(',')
            #        role, created = Role.objects.get_or_create(name='Witness')
             #       witness_person, created = Person.objects.get_or_create(first_name=first,last_name=last,role=role)  
              #      manumission.person.add(witness_person)
                    
                        
        # strip spaces from persons
        for person in Person.objects.all():
            if person.first_name: 
                person.first_name = person.first_name.strip()
            if person.last_name:
                person.last_name = person.last_name.strip()
            person.save()

        self.stdout.write(self.style.SUCCESS('Done'))
