"""photoServiceSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from .admin import  myems_admin_site
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from client.views import (
    ClientViewSet,
    SizeViewSet,
    CityViewSet,
    AddressesViewSet,
    ImageViewSet,
    OrderViewSet,
    OrderStatusViewSet,
    ImageGroupViewSet,
    login,
    getMe,
    create_order
    )
router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'size', SizeViewSet)
router.register(r'city', CityViewSet)
router.register(r'addresses', AddressesViewSet)
router.register(r'image', ImageViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderstatus', OrderStatusViewSet)
router.register(r'imagegroup', ImageGroupViewSet)
urlpatterns = [
    path('', myems_admin_site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/client-login/',login),
    path('api/client-get/me/',getMe),
    path('api/client-create/order/',create_order)


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
