from django.db import models
from book_management_system.model import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
