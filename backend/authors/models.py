
from django.db import models

from users.models import User


class Author(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="author",
    )

    def __str__(self):
        return f"Author: {self.user.__str__()}"

