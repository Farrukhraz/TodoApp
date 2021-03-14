from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    # author_user = serializers.StringRelatedField()
    # developer_user = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', ]