from rest_framework.viewsets import ModelViewSet

from .models import Project
from .serializers import ProjectSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
