from django.utils import timezone

from django.db import models

from todos.models import Ticket
from developers.models import Developer


class Project(models.Model):
    name = models.CharField(verbose_name='name', max_length=64)
    description = models.TextField(blank=True)
    tickets = models.ManyToManyField(Ticket)
    developers = models.ManyToManyField(Developer)
    repo_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"'{self.name}' project. Number of tickets: {self.tickets.count()}. "
               # FIXME Find out how to get project developers properly!
               # f"Participating developers: {self.developers.all()}"
