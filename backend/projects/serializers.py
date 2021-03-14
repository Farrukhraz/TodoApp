from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'

    # ToDo return list of tickets.
    #  Example link: /api/projects/1/
