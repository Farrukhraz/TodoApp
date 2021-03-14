from rest_framework import serializers

from .models import Project
from developers.serializers import DeveloperSerializer
from todos.serializers import TicketSerializer


class ProjectSerializer(serializers.ModelSerializer):
    tickets = serializers.StringRelatedField(many=True)
    developers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        tickets = TicketSerializer
        developers = DeveloperSerializer
        fields = '__all__'

    # ToDo return list of tickets.
    #  Example link: /api/projects/1/
