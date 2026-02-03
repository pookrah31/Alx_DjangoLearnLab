from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from django.urls import reverse


class BookAPITestCase(TestCase):
    """Unit tests for Book API endpoints"""

    def setUp(self):
        """Create test data and users"""
        # Test client
        self.client = APIClient()

        # Create users
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.admin = User.objects.create_superuser(username="admin", password="admin123")

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(
            title="Django Basics", publication_year=2022, author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Python Advanced", publication_year=2023, author=self.author2
        )

        # URLs
        self.list_url = reverse("book-list")  # assuming name='book-list'
        self.create_url = reverse("book-create")
        self.detail_url = lambda pk: reverse("book-detail", args=[pk])
        self.update_url = lambda pk: reverse("book-update", args=[pk])
        self.delete_url = lambda pk: reverse("book-delete", args=[pk])

    # -------------------------------
    # List and filtering tests
    # -------------------------------
    def test_list_books_unauthenticated(self):
        """Anyone can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_author(self):
        """Filter books by author"""
        response = self.client.get(self.list_url, {"author": self.author1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Basics")

    def test_search_books_by_title(self):
        """Search books by text"""
        response = self.client.get(self.list_url, {"search": "Python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Python Advanced")

    def test_order_books_by_publication_year(self):
        """Test ordering books"""
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 2023)

    # -------------------------------
    # Create book tests
    # -------------------------------
    def test_create_book_authenticated(self):
        """Authenticated user can create a book"""
        self.client.login(username="testuser", password="password123")
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author1.id,
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_create_book_unauthenticated(self):
        """Unauthenticated user cannot create a book"""
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author1.id,
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------------
    # Retrieve book tests
    # -------------------------------
    def test_retrieve_book(self):
        """Retrieve book details"""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django Basics")

    # -------------------------------
    # Update book tests
    # -------------------------------
    def test_update_book_authenticated(self):
        """Authenticated user can update a book"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Updated Book"}
        response = self.client.put(self.update_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        """Unauthenticated user cannot update a book"""
        data = {"title": "Updated Book"}
        response = self.client.put(self.update_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------------
    # Delete book tests
    # -------------------------------
    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book"""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Unauthenticated user cannot delete a book"""
        response = self.client.delete(self.delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 2)
