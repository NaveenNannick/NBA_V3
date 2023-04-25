from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm


class LoginFormTest(TestCase):

    def test_login_form_valid(self):
        form_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form_data = {
            'username': '',
            'password': ''
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())


class SignUpFormTest(TestCase):

    def test_signup_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid(self):
        form_data = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': ''
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

class RegisterUserViewTest(TestCase):

    def test_register_user_view(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, 'Create an account')

    def test_register_user_form_valid(self):
        url = reverse('register')
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/login/', fetch_redirect_response=False)

    def test_register_user_form_invalid(self):
        url = reverse('register')
        form_data = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': ''
        }
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Form is not valid')



class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.form_data = {'username': 'testuser', 'password': 'testpass'}
        self.invalid_form_data = {'username': 'testuser', 'password': 'invalidpass'}
        self.empty_form_data = {'username': '', 'password': ''}

    def test_login_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_login_view_post_valid_form(self):
        response = self.client.post(self.url, self.form_data)
        self.assertRedirects(response, '/profiles/profile/')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_post_invalid_form(self):
        response = self.client.post(self.url, self.invalid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)
        self.assertContains(response, 'Invalid credentials')

    def test_login_view_post_empty_form(self):
        response = self.client.post(self.url, self.empty_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)
        


class RegisterUserViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')
        self.valid_form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpass',
            'password2': 'testpass'
        }
        self.invalid_form_data = {
            'username': '',
            'email': 'invalidemail',
            'password1': 'short',
            'password2': 'notmatching'
        }

    def test_register_user_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertIsInstance(response.context['form'], SignUpForm)

    def test_register_user_view_post_valid_form(self):
        response = self.client.post(self.url, self.valid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '')
        self.assertEqual(User.objects.count(), 2)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_user_view_post_invalid_form(self):
        response = self.client.post(self.url, self.invalid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertIsInstance(response.context['form'], SignUpForm)
        

