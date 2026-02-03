from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# -------------------------------
# List all books (read-only for everyone)
# -------------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Returns a list of all Book instances.

    - Accessible to unauthenticated users (read-only)
    - Supports filtering by author and publication year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering
    filter_backends = [DjangoFilterBackend]
    filters_fields = ['author', 'publication_year']
    
      # Enable search functionality
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']

    
    # Ordering configuration
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering



     # 1️⃣ Filterable fields
    filters_fields = ['title', 'author', 'publication_year']

    # 2️⃣ Searchable fields
    search_fields = ['title', 'author__name']

    # 3️⃣ Ordering fields (front-end can request ordering)
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


# -------------------------------
# Retrieve details of a single book
# -------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Returns details of a single Book instance.

    Read-only; accessible to unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------------------
# Create a new book (authenticated users only)
# -------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Creates a new Book instance.

    Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

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
    Deletes a Book instance.

    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
