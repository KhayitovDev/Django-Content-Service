from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, BlogViewSet, NewsViewSet

router=DefaultRouter()
router.register(r"categories", CategoryViewSet, basename='course')
router.register(r"tags", TagViewSet, basename='tag')
router.register(r"blog", BlogViewSet, basename='blog')
router.register(r"news", NewsViewSet, basename='news')

urlpatterns = [
    path('api/', include(router.urls) )
]
