from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

from catalog.models import Person

class PersonListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons for pagination tests
        number_of_persons = 13

        for person_id in range(number_of_persons):
            Person.objects.create(
                first_name=f'Christian {person_id}',
                last_name=f'Surname {person_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/persons/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('persons'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('persons'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/person_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('persons'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['person_list']) == 10)

    def test_lists_all_persons(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('persons')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['person_list']) == 3)

import datetime

from django.utils import timezone
from django.contrib.auth.models import User # Required to assign User as a borrower

from catalog.models import Manumission, Role, Gender
        
        # Create a manumission
        test_person = Person.objects.create(first_name='John', last_name='Smith')
        test_role = Role.objects.create(name='Witness')
        test_gender = Gender.objects.create(name='Male')
        test_manumission = Manumission.objects.create(
            title='Book Title',
            person=test_person,
            gender=test_gender,
        )

        # Create role as a post-step
        role_objects_for_manumission = Role.objects.all()
        test_manumission.role.set(role_objects_for_manumission) # Direct assignment of many-to-many types not allowed.
        test_manumission.save()
        
#    def test_redirect_if_not_logged_in(self):
#        response = self.client.get(reverse('my-borrowed'))
#        self.assertRedirects(response, '/accounts/login/?next=/catalog/mybooks/')

#    def test_logged_in_uses_correct_template(self):
#        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#        response = self.client.get(reverse('my-borrowed'))
        
        # Check our user is logged in
#        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
#        self.assertEqual(response.status_code, 200)

        # Check we used correct template
#        self.assertTemplateUsed(response, 'catalog/bookinstance_list_borrowed_user.html')