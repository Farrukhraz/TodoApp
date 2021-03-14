from rest_framework.viewsets import ModelViewSet

from .models import Developer
from .serializers import DeveloperSerializer


class DeveloperModelViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
