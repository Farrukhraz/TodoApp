
from django.db import models

from users.models import User


class Author(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"Author: {User.first_name} {User.last_name}."

