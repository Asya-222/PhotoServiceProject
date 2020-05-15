
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

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes 
from rest_framework.permissions import IsAuthenticated 
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER 
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from rest_framework_jwt.settings import api_settings
from django.http import JsonResponse
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
from django.contrib.auth import authenticate, get_user_model
from rest_framework import exceptions
from django_filters import rest_framework as filters


import django_filters

factory = APIRequestFactory()

request = factory.get('/')


serializer_context = {

    'request': Request(request),
}


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ["client"]

class AddressesFilter(django_filters.FilterSet):
    class Meta:
        model = Addresses
        fields = ["client"]


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
    
    def perform_destroy(self, instance):
        user = instance.user
        instance.delete()
        user.delete()



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
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AddressesFilter



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
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = OrderFilter

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



@api_view(['POST'])
def login(request):
    print("ASdaskdjkalsjdasdkljsakdjsakldjksaldjklsj")
    username = request.data.get('username', None)
    password = request.data.get('password', None)
    if not username or not password:
        raise exceptions.AuthenticationFailed(('No credentials provided.'))

    credentials = {
        get_user_model().USERNAME_FIELD: username,
        'password': password
    }


    user = authenticate(**credentials)
    if user is None:
        raise exceptions.AuthenticationFailed(('Invalid username/password.'))

    if not user.is_active:
        raise exceptions.AuthenticationFailed(('User inactive or deleted.'))

    try:
        client = Client.objects.get(user=user)
    except:
        raise exceptions.AuthenticationFailed(('Invalid username/password.'))

    
    refresh = RefreshToken.for_user(user)
    return JsonResponse({
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    })


@api_view(['POST'])
def create_order(request):

    order = request.data.get('order')
    group_image = request.data.get('group_image')
 
    order_serilizer = OrderSerializer(
        data=dict(order), context=serializer_context)
    if order_serilizer.is_valid():
        order_serilizer.save()
        print(order_serilizer.data,'-------------')
        order_url = order_serilizer.data.get('url')
        if len(group_image) > 0:

            for target_list in group_image:
                target_list['order'] = order_url
                group_image_serializer = ImageGroupSerializer(
                    data=target_list, context=serializer_context)
                if group_image_serializer.is_valid():
                    group_image_serializer.save()
                else:
                    return Response(group_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(order_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({
        'message': 'ok'
    })

@api_view(['GET']) 
@permission_classes((IsAuthenticated,))
def getMe(request):
    try:
        user = Client.objects.get(user=request.user).get_fields()
    except ObjectDoesNotExist:
        return JsonResponse({
            'message': 'User not found',
        }, status=404)

    return JsonResponse({
            'message': 'ok',
            'data': user
        }, status=200)


