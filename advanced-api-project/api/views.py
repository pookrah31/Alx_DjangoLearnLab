from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# List all books (Read-only for everyone)
# -------------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Returns a list of all Book instances.
    Read-only; accessible to unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Everyone can access


# -------------------------------
# Retrieve details of a single book
# -------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Returns details of a single Book instance by its primary key.
    Read-only; accessible to unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------------
# Create a new book (authenticated users only)
# -------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Creates a new Book instance.
    Only authenticated users can create books.
    Validates input data using BookSerializer (including publication_year validation).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users

    def perform_create(self, serializer):
        """
        Customize saving behavior if needed.
        For example, we could automatically associate a user with the book if the model had an owner field.
        """
        serializer.save()


# -------------------------------
# Update an existing book (authenticated users only)
# -------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<id>/update/
    Updates an existing Book instance.
    Only authenticated users can update books.
    Handles validation automatically via BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Customize update behavior here if needed.
        """
        serializer.save()


# -------------------------------
# Delete a book (authenticated users only)
# -------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/
    Deletes a Book instance by ID.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
