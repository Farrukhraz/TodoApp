from rest_framework.viewsets import ModelViewSet

from .models import Ticket
from .serializers import TicketSerializer


# class ListTodo(generics.ListCreateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#
#
# class DetailedTodo(generics.RetrieveAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer


class TicketModelViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
