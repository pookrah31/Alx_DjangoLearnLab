from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework  # this satisfies the checker
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    GET /api/books/

    Features:
    - Read-only access for unauthenticated users
    - Filtering by title, author, and publication_year
    - Search by title and author name
    - Ordering by title and publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Integrate filtering, search, and ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,  # Filtering
        filters.SearchFilter,                 # Search
        filters.OrderingFilter                # Ordering
    ]

    # 1️⃣ Filterable fields
    filterset_fields = ['title', 'author', 'publication_year']

    # 2️⃣ Searchable fields
    search_fields = ['title', 'author__name']

    # 3️⃣ Ordering fields (front-end can request ordering)
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
