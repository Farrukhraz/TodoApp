from django.db import models

from users.models import User


class Developer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="developer",
    )
    grade = models.CharField(verbose_name="Grade", max_length=32, default='Unknown')
    level = models.CharField(verbose_name="Level", max_length=32, default='Junior')

    def __str__(self):
        return f"Developer: {self.user.__str__()}."


