from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from django.db.models import QuerySet

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


from borrowings.models import Borrowing
from borrowings.serializers import (
    BorrowingSerializer,
    BorrowingDetailSerializer,
    BorrowingListSerializer,
    BorrowingReturnSerializer,
)
from borrowings.permissions import IsAdminOrIfAuthenticatedReadOnly


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    @staticmethod
    def _filtering(queryset: QuerySet, is_active_borrowing: str) -> QuerySet:
        if is_active_borrowing == "True":
            return queryset.filter(actual_return_date__isnull=True)
        elif is_active_borrowing == "False":
            return queryset.filter(actual_return_date__isnull=False)
        return queryset

    def get_queryset(self):
        queryset = self.queryset
        is_active = self.request.query_params.get("is_active")
        user_id = self.request.query_params.get("user_id")

        if self.request.user.is_staff:
            if user_id:
                queryset = queryset.filter(user_id=int(user_id))
            if is_active:
                queryset = self._filtering(queryset, is_active)
        else:
            queryset = queryset.filter(user=self.request.user)
            if is_active:
                queryset = self._filtering(queryset, is_active)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        elif self.action == "retrieve":
            return BorrowingDetailSerializer
        elif self.action == "return_book":
            return BorrowingReturnSerializer
        return BorrowingSerializer

    @action(
        methods=["PATCH"],
        detail=True,
        url_path="return",
        permission_classes=[IsAdminUser],
    )
    def return_book(self, request, pk=None):
        borrowing = self.get_object()
        serializer = self.get_serializer(borrowing, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="is_active",
                type=OpenApiTypes.STR,
                description="Filter by active borrowings (ex. ?is_active=True)",
            ),
            OpenApiParameter(
                "user_id",
                type=OpenApiTypes.INT,
                description="Filter by user id if auth as admin (ex. ?user_id=1)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
