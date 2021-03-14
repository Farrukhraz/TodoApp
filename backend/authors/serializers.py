from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = '__all__'
