

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User, Group
from .models import Book

class PermissionTests(TestCase):
    def setUp(self):
        # Create user and groups
        self.viewer = User.objects.create_user('viewer', 'viewer@test.com', 'password123')
        self.editor = User.objects.create_user('editor', 'editor@test.com', 'password123')
        self.admin = User.objects.create_superuser('admin', 'admin@test.com', 'password123')

        viewers_group = Group.objects.get(name='Viewers')
        editors_group = Group.objects.get(name='Editors')
        self.viewer.groups.add(viewers_group)
        self.editor.groups.add(editors_group)

        # Create a book
        self.book = Book.objects.create(title='Test Book', author='Author', publication_year=2026)

    def test_view_permission(self):
        self.client.login(username='viewer', password='password123')
        response = self.client.get(f'/books/{self.book.id}/view/')
        self.assertEqual(response.status_code, 200)
