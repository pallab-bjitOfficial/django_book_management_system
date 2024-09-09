from django.db import models
from author.models import Author
from book_management_system.model import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
