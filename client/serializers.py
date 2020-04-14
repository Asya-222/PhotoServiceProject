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

from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AddressesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ImageGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageGroup
        fields = '__all__'