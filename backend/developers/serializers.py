from rest_framework import serializers

from .models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Developer
        fields = '__all__'
