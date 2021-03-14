from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    serializers.StringRelatedField(many=True)

    class Meta:
        model = Ticket
        fields = '__all__'
