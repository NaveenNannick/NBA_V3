from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from calc.models import CAY
from profiles.models import Profile

class CalcAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.profile = Profile.objects.create(
            user=self.user,
            department='MCA',
            designation=1,
            phd=1,
            yearofjoining=date(2015, 1, 1),
            oneweek=1,
            twoweek=0,
            interaction=5
        )
        self.cay = CAY.objects.create(
            year=date.today(),
            STR=1,
            FCR=2,
            FQ=3,
            FR=4,
            FP=5,
            IWO=6
        )

    def test_dashboard_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertContains(response, 'Dashboard')

    def test_avg_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('avg'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'avgcay.html')
        self.assertContains(response, 'Current Academic Year')

    def test_dashboard_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('dashboard'), {'1sty': 10, '2ndy': 20, '3rdy': 30})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertContains(response, 'Dashboard')

    def test_avg_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('avg'), {'1y': 10, '2y': 20, '3y': 30})
        print(response.content)
        self.assertEqual(response.status_code, 302)
        print(CAY.objects.count())
        cay = CAY.objects.first()
        print(cay)
        self.assertIsNotNone(cay)
        


