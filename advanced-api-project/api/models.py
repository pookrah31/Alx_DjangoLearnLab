from django.db import models

# Author model
# Represents a writer who can have one or more books.
# This is the "parent" in a one-to-many relationship with Book.
class Author(models.Model):
    # Stores the name of the author
    name = models.CharField(max_length=255)

    # String representation of the Author
    # Makes the author name readable in the admin panel and shell
    def __str__(self):
        return self.name


# Book model
# Represents a book written by an author.
# Each book is linked to exactly one author (one-to-many relationship).
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)
    
    # Year the book was published
    publication_year = models.IntegerField()
    
    # ForeignKey establishes a one-to-many relationship:
    # - One author can have many books
    # - Each book belongs to one author
    # on_d_
