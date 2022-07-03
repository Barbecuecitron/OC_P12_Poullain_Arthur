"""epic_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .router import *
from dj_rest_auth.views import LogoutView
from dj_rest_auth.urls import LoginView
from dj_rest_auth.urls import *
from rest_framework.authtoken import views

# from rest_framework.urls import LoginView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token, name="api-token-auth")
    # path("logout/", LogoutView.as_view(), name="logout"),
    # path("login/", LoginView.as_view(), name="Login"),
    # path("api/", include("dj_rest_auth.urls"))
    # path("api-token-auth/", views.obtain_auth_token),
]
