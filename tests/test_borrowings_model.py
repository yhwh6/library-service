from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIClient

from books.models import Book
from borrowings.models import Borrowing


class BorrowingModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "qwerty123",
        )

        self.his_dark = Book.objects.create(
            title="Chronicles of Siala",
            author="Alexey Pehov",
            cover="Hard",
            inventory=9,
            daily_fee=3,
        )

    def test_validation_date(self):
        borrow_date = datetime(year=2023, month=1, day=9).date()
        expected_return_date = datetime(year=2023, month=1, day=8).date()

        try:
            Borrowing.objects.create(
                user=self.user,
                book=self.his_dark,
                borrow_date=borrow_date,
                expected_return_date=expected_return_date,
            )
        except ValidationError as ve:
            self.assertEqual(
                ve.messages,
                ["The expected return date must be greater than or equal to the borrow date."],
            )
