from rest_framework import viewsets

from books.models import Book
from books.serializers import (
    BookSerializer,
    BookListSerializer,
)
from books.permissions import IsAdminOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in (
            "list",
            "retrieve",
        ):
            return BookListSerializer
        return BookSerializer
