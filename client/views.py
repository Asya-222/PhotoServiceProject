
from .serializers import (
    ClientSerializer,
    CitySerializer,
    AddressesSerializer,
    ImageSerializer,
    OrderSerializer,
    OrderStatusSerializer,
    SizeSerializer,
    ImageGroupSerializer
)
from .models import (
    Client,
    City,
    Addresses,
    Image,
    Order,
    OrderStatus,
    Size,
    ImageGroup
)
from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status

from rest_framework.request import Request
from rest_framework import generics
from rest_framework.test import APIRequestFactory
from rest_framework.response import Response
factory = APIRequestFactory()

request = factory.get('/')


serializer_context = {

    'request': Request(request),

}

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in "GET"


class WreadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in "POST"

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Gallery to be viewed or edited.
    """
    # permission_classes = (ReadOnly,WreadOnly)

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    """
    # permission_classes = (WreadOnly,ReadOnly)

    queryset = City.objects.all()
    serializer_class = CitySerializer


class AddressesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    # """
    # permission_classes = (WreadOnly,ReadOnly)

    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    """
    # permission_classes = (WreadOnly,ReadOnly)

    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    """
    # permission_classes = (WreadOnly,ReadOnly)

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    """
    # permission_classes = (WreadOnly,ReadOnly)

    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class SizeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    """
    # permission_classes = (WreadOnly,ReadOnly)

    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ImageGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    """
    # permission_classes = (WreadOnly,ReadOnly)

    queryset = ImageGroup.objects.all()
    serializer_class = ImageGroupSerializer