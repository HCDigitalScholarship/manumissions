from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns


class Role(models.Model):
    """Model representing the roles individuals listed in our manumissions (e.g. enslaver, enslaved person, witness, scribe, etc)."""
    name = models.CharField(max_length=200,
        help_text="Enter a person's role"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Person(models.Model):
    """Model representing Names listed in our manumission documents (e.g. )."""
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    alt_spelling_first_name = models.CharField(max_length=100, null=True, blank=True)
    alt_spelling_last_name = models.CharField(max_length=100, null=True, blank=True)
    abbreviated_first_name = models.CharField(max_length=100, null=True, blank=True)
    abbreviated_last_name = models.CharField(max_length=100, null=True, blank=True)

    role = models.ManyToManyField(Role, help_text="Select a role for this person")
    # ManyToManyField used because a Role can contain many People and a Person can cover many roles.
    # Role class has already been defined so we can specify the object above.

    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because a person will have one gender listed, but genders will correspond to multiple people
    birth_place = models.ForeignKey('Birth_Place', on_delete=models.SET_NULL, null=True, blank=True)
    death_place = models.ForeignKey('Death_Place', on_delete=models.SET_NULL, null=True, blank=True)
    place_freed= models.ForeignKey('Place_Freed', on_delete=models.SET_NULL, null=True)
    age_freed= models.CharField('Age_Freed', max_length=30, help_text='Age when freedom occured', blank=True)
    age_listed= models.CharField('Age_Listed', max_length=30, help_text='Age listed on the Manumission Document', blank=True)
    year_manumitted= models.CharField('Year Manumission took effect', max_length=10, help_text='Year when freedom occured', blank=True)

    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    
    def display_role(self):
        """Create a string for the Role. This is required to display roles in Admin."""
        return ', '.join(role.name for role in self.role.all()[:3])
    
    display_role.short_description = 'Roles played in any manumissions'

    class Meta:
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
        """Returns the url to access a particular person."""
        return reverse('person-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)

class Manumission(models.Model):
    """"Model representing information from discreet manumission documents."""
    title = models.CharField(max_length=300, null=True)
    date_of_manumission_signing = models.DateField(null=True, blank=True)
    image_name = models.ForeignKey('Image_Name', on_delete=models.SET_NULL, null=True)
    person = models.ManyToManyField(Person, help_text="Select Persons for this Manumission")
    # ManyToManyField used because an person can be involved in many manumissions and a manumission can involve many persons.
    # Person class has already been defined so we can specify the object above.
    monthly_meeting = models.ForeignKey('Monthly_Meeting', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because a Manumission can only have one Monthly Meeting, but Monthly Meetings will hold many manumissions.
    # Name as a string rather than object because it hasn't been declared yet in file.
    page_number = models.ForeignKey('Page_Number', on_delete=models.SET_NULL, null=True)
    call_number = models.ForeignKey('Call_Number', on_delete=models.SET_NULL, null=True)

    def display_person(self):
        """Create a string for the Person. This is required to display persons in Admin."""
        return ', '.join(person.first_name for person in self.person.all()[:3])
    
    display_person.short_description = 'Persons involved in Manumission'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this manumission."""
        return reverse('manumission-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title

class Gender(models.Model):
    """Model representing the assumed gender of individuals listed in our manumissions (e.g. male, female)."""
    gender = models.CharField(max_length=200,
        help_text="Enter the assumed gender of the respective person"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.gender

class Image_name(models.Model):
    """Model representing the names of digital images in our archive."""
    image_name = models.CharField(max_length=200,
        help_text="Enter the image/scan name for the manumission (e.g. HC10-1000X_XXX.)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.image_name

class Page_Number(models.Model):
    """Model representing the Physical page numbers in our archive."""
    page_number = models.CharField(max_length=200,
        help_text="Enter the Page Numbe listed in the Physical manumission book for the respective manumission"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.page_number

class Birth_Place(models.Model):
    """Model representing the place someone was born."""
    birth_place = models.CharField(max_length=200,
        help_text="Enter the Birth place of the respective person"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.birth_place

class Death_Place(models.Model):
    """Model representing the place someone Died."""
    death_place = models.CharField(max_length=200,
        help_text="Enter the Death Place of the respective person"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.death_place

class Age_Listed(models.Model):
    """Model representing the age listed of the individual on the manumission."""
    age_listed = models.CharField(max_length=200,
        help_text="Enter the age  listed on the manumission of the respective person"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.age_listed

class Age_Freed(models.Model):
    """Model representing the age the individual when freed from enslavement."""
    age_freed = models.CharField(max_length=200,
        help_text="Enter the age of the respective person at their freed date"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.age_freed

class Year_Manumitted(models.Model):
    """Model representing the year when freed from enslavement."""
    year_manumitted = models.CharField(max_length=200,
        help_text="Enter the Year of their freed date"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.year_manumitted

class Place_Freed(models.Model):
    """Model representing the place where freed from enslavement."""
    place_freed = models.CharField(max_length=200,
        help_text="Enter the Place where their manumission took place"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.place_freed

class Monthly_Meeting(models.Model):
    """Model representing the Monthly Meeting of discreet manumission documents."""
    monthly_meeting = models.CharField(max_length=200,
        help_text="Enter the Monthly Meeting listed on the manumission documents"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.monthly_meeting

class Call_Number(models.Model):
    """Model representing the Call Number of discreet manumission documents."""
    call_number = models.CharField(max_length=200,
        help_text="Enter the Call Number associated with the manumission document"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.call_number
