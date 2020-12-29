from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=52)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

