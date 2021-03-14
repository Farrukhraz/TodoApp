from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authors.views import AuthorModelViewSet
from developers.views import DeveloperModelViewSet
from projects.views import ProjectModelViewSet
from todos.views import TicketModelViewSet
from users.views import UserModelViewSet

def trigger_error(request):
    return 1 / 0


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('developers', DeveloperModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TicketModelViewSet)
router.register('users', UserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('sentry-error/', trigger_error),
]
