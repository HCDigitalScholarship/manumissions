from django.test import TestCase

from catalog.models import Person

class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Person.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        person=Person.objects.get(id=1)
        field_label = person._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        person = Person.objects.get(id=1)
        expected_object_name = f'{person.last_name}, {person.first_name}'
        self.assertEquals(expected_object_name, str(person))

    def test_get_absolute_url(self):
        person = Person.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(person.get_absolute_url(), '/catalog/person/1')