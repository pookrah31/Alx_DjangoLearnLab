from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# List all books (read-only for everyone)
# -------------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Returns a list of all Book instances.
    Read-only; accessible to unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Everyone can access


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
    permission_classes = [AllowAny]


# -------------------------------
# Create a new book (authenticated users only)
# -------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Creates a new Book instance.
    Only authenticated users can create books.
    Validates input data using BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users

    def perform_create(self, serializer):
        serializer.save()


# -------------------------------
# Update an existing book (authenticated users only)
# -------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<id>/update/
    Updates an existing Book instance.
    Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
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
    permission_classes = [IsAuthenticated]
