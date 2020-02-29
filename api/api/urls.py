from django.contrib import admin
from django.urls import path, include
from core.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
