from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import home, dashboard, user
from django.contrib.auth.models import User

import pytest

# Create your tests here.
class testCases(SimpleTestCase):

    # tes url
    def testHomeUrl(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)
    def testDashboardUrl(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, dashboard)
    def testUserUrl(self):
        url = reverse('user')
        self.assertEqual(resolve(url).func, user)


    # test user outside testclass
@pytest.mark.django_db
def testCreateUser():
    User.objects.create_user('agri2', 'afryanto@email.com', '123456')
    assert User.objects.count() == 1



    
