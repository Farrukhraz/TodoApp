from django.db import models


class User(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=32)
    last_name = models.CharField(verbose_name='Last name', max_length=32)
    birth_date = models.DateField(verbose_name='Birth date')

    def __str__(self):
        return f"{self.first_name} {self.last_name}. Birth date: {self.birth_date}"

