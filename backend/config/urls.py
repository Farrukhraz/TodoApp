from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet
from todos.views import TicketModelViewSet


def trigger_error(request):
    return 1 / 0


router = DefaultRouter()
# router.register('authors', AuthorModelViewSet)
router.register('todos', TicketModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('sentry-error/', trigger_error),
]
