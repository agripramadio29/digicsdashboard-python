from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import *
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
    def testParameterSistemUrl(self):
        url = reverse('sysparam')
        self.assertEqual(resolve(url).func, sysparam)
    def testTerminalListUrl(self):
        url = reverse('terminallist')
        self.assertEqual(resolve(url).func, terminallist)
    def testCardTypeUrl(self):
        url = reverse('cardtype')
        self.assertEqual(resolve(url).func, cardtype)
    def testReportUrl(self):
        url = reverse('report')
        self.assertEqual(resolve(url).func, report)
    def testAccountReportUrl(self):
        url = reverse('accountreport')
        self.assertEqual(resolve(url).func, accountreport)
    def testRegistrationReportUrl(self):
        url = reverse('registrationreport')
        self.assertEqual(resolve(url).func, registrationreport)        


    # test user outside testclass
@pytest.mark.django_db
def testCreateUser():
    User.objects.create_user('agri2', 'afryanto@email.com', '123456')
    assert User.objects.count() == 1



    
