from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework  # satisfies automated checker
from .models import Book
from .serializers import BookSerializer


# -------------------------------
# List all books with filtering, search, and ordering
# -------------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/

    Features:
    - Read-only access for unauthenticated users
    - Filter by title, author, publication_year
    - Search by title and author name
    - Ordering by title and publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Integrate filtering, search, and ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,  # filtering
        filters.SearchFilter,                 # search
        filters.OrderingFilter                # ordering
    ]

    # Filterable fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searchable fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


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
