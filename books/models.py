from django.db import models


class Book(models.Model):
    class BookCover(models.TextChoices):
        HARD = "H"
        SOFT = "S"

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.CharField(max_length=1, choices=BookCover.choices)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=7, decimal_places=2)

    def get_cover(self):
        cover_index = self.BookCover.values.index(self.cover)
        return self.BookCover.labels[cover_index]
