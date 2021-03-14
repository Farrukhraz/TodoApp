from typing import List, Tuple

from django.db import models

from authors.models import Author
from developers.models import Developer


class Ticket(models.Model):
    title = models.CharField(max_length=52)
    content = models.TextField(blank=True)
    authors = models.ManyToManyField(Author)
    developers = models.ManyToManyField(Developer)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        content = f"Ticket: title: {self.title};"
        # many_to_many_fields = ['authors', 'developers', ]
        # content += self.__get_many_to_many_field_values(many_to_many_fields)
        return content

    def __get_many_to_many_field_values(self, field_names: List[str]) -> str:
        field_values = ''
        for name in field_names:
            try:
                result = eval(f"self.{name}.all()")
                result = f"{name}: {result}"
            except ValueError:
                continue
            field_values += result
        return field_values

