from django.test import SimpleTestCase, TestCase
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
         
    @pytest.mark.skip(reason="skip intended")
    def testUserUrl(self):
        url = reverse('user')
        self.assertEqual(resolve(url).func, user)
    # def testParameterSistemUrl(self):
    #     url = reverse('sysparam')
    #     self.assertEqual(resolve(url).func, sysparam)
    # def testTerminalListUrl(self):
    #     url = reverse('terminallist')
    #     self.assertEqual(resolve(url).func, terminallist)
    # def testCardTypeUrl(self):
    #     url = reverse('cardtype')
    #     self.assertEqual(resolve(url).func, cardtype)
    # def testReportUrl(self):
    #     url = reverse('report')
    #     self.assertEqual(resolve(url).func, report)
    # def testAccountReportUrl(self):
    #     url = reverse('accountreport')
    #     self.assertEqual(resolve(url).func, accountreport)
    # def testRegistrationReportUrl(self):
    #     url = reverse('registrationreport')
    #     self.assertEqual(resolve(url).func, registrationreport)

    # test login
class LoginViewTest(TestCase):
    @classmethod
    def setup(cls):
        cls.username = 'admin'
        cls.password = '123456'
        cls.user = User.objects.create_user(username=cls.username, password=cls.password)

    def test_successful_login(self):
        response = self.client.post(reverse('home'), {'username': 'admin', 'password': '123456'})
        #self.assertRedirects(response, reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    # def test_failed_password(self):
    #     response = self.client.post(reverse('home'), {'username':'admin', 'password':'edita'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Password is Incorrect!')
    def test_failed_login(self):
        response = self.client.post(reverse('home'), {'username': 'alfian', 'password': 'edita'})
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'password')
        self.assertContains(response, 'Username or Password is Incorrect!')

    # test user outside testclass
# @pytest.mark.django_db
# def testcreateuser():
#     User.objects.create_user('agri2', 'afryanto@email.com', '123456')
#     assert User.objects.count() == 1





    
