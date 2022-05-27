from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import TodoViewset

router = DefaultRouter()
router.register(r'api', TodoViewset, basename='api')
urlpatterns = [
    path('', include(router.urls))
]

