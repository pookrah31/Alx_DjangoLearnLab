from django.contrib import admin

# Register your models here.

from .models import Author, Book

# Register Author and Book models to access them in the admin
admin.site.register(Author)
admin.site.register(Book)
