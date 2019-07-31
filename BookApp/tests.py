from django.test import TestCase
from .models import Book, Author
from django.contrib.auth.models import User
from decimal import *
# Create your tests here.

class StoreViewsTestCase(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(
            username="james", email="some@email.com", password="password"
        )
        author = Author.objects.create(first_name="Alexander", last_name="Sikander")
        book = Book.objects.create(title="How to Conquer the World with Alexander", author=author, description="Let's win it", price=1000, stock=1)

    def test_index(self):
        resp = self.client.get('/BookApp/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('books' in resp.context)
        self.assertTrue(resp.context['books'].count() > 0)

    def test_cart(self):
        resp = self.client.get('/BookApp/cart/')
        self.assertEqual(resp.status_code, 302)

    def test_book_detail(self):
        resp = self.client.get('/BookApp/book/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['book'].pk, 1)
        self.assertEqual(resp.context['book'].title, "How to Conquer the World with Alexander")

    def test_add_to_cart(self):
        self.logged_in=self.client.login(username="james", password="password")
        self.assertTrue(self.logged_in)
        resp = self.client.get('/BookApp/add/1')
        resp = self.client.get('/BookApp/cart/1')
        self.assertEqual(resp.context['total'], Decimal('1000.00'))
        self.assertEqual(resp.context['count'], 1)
        self.assertEqual(resp.context['cart'].count(), 1)
        self.assertEqual(resp.context['cart'].get().quantity, 1)