from rest_framework import generics

from .models import Ticket
from .serializers import TicketSerializer


class ListTodo(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class DetailedTodo(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
