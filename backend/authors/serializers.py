from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Author
        fields = '__all__'
