from rest_framework import serializers

from .models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    serializers.StringRelatedField(many=True)

    class Meta:
        model = Developer
        fields = '__all__'
