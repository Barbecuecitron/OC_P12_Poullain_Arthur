# from dj_rest_auth.views import (
#     LoginView, LogoutView)
from rest_framework import routers
from apps.clients.views import ClientViewSet
from django.urls import include, path
router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet, basename="clientsview")

urlpatterns = [
    path('', include(router)),
]

