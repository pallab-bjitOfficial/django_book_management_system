from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')

urlpatterns = [
    path('', include(router.urls)),
]
