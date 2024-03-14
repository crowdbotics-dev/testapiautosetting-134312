from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134312ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134312", Testconnectors134312ViewSet, basename="testconnectors134312"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
