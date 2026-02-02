from rest_framework import serializers
from .models import Author, Book

# Serializer for the Book model
# Converts Book instances to JSON and validates incoming book data
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        # Serializes all fields: id, title, publication_year, author
        fields = "__all__"

    # Custom field-level validation
    # Ensures that the publication year is not in the future
    # This protects against invalid data entry
    def validate_publication_year(self, value):
        if value > 2024:  # You could replace 2024 with dynamic current year
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# Serializer for the Author model
# Includes the author's name and all related books (nested serialization)
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to dynamically include all books for an author
    # many=True because one author can have multiple books
    # read_only=True to prevent creating books via AuthorSerializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        # Include author's id, name, and the nested books
        fields = ['id', 'name', 'books']
