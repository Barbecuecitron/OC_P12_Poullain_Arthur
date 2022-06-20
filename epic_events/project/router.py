# from dj_rest_auth.views import (
#     LoginView, LogoutView)
from rest_framework import routers
from apps.clients.views import ClientViewSet
from apps.contracts.views import ContractViewSet
from django.urls import include, path
router = routers.DefaultRouter()

router.register(r'clients', ClientViewSet, basename="clientsview")
router.register(r'contracts', ContractViewSet, basename="contractsview")


urlpatterns = [
    path('', include(router)),
]

