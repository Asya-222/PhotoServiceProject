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
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db import transaction 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, required=False
    )

    email = serializers.EmailField(required=False)
    class Meta:    
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            
        )


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Client  
        fields = (
            'id',
            'url',
            'user'
        )

    def create(self, validated_data):

        try:

            validated_data['user'] = User.objects.create(
                first_name=validated_data.get('user')['first_name'],
                last_name=validated_data.get('user')['last_name'],
                email=validated_data.get('user')['email'],
                password=make_password(validated_data.get('user')['password']),
                username=validated_data.get('user')['email']

            )
        except IntegrityError as e: 
            raise serializers.ValidationError(e)

        instance = Client.objects.create(**validated_data)

        return instance    


    @transaction.atomic
    def update(self, instance, validated_data):

        print(validated_data.get('user')['first_name'])
        Client.objects.filter(id=instance.user.id).update(first_name=validated_data.get('user')['first_name'],
                                                        last_name=validated_data.get('user')['last_name'])
        instance.__dict__.update(**validated_data)
        instance.save()
        return instance


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




class OrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ImageGroupSerializer(serializers.HyperlinkedModelSerializer):
    size_image_group = SizeSerializer(source='size',read_only=True)
    class Meta:
        model = ImageGroup
        fields = ('quantity','size','order','images','size_image_group')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    
    group_image = ImageGroupSerializer(many=True,read_only=True)
    status = OrderStatusSerializer(source='order_status',read_only=True)

    class Meta:
        model = Order
        fields = ('url','address','id','amount','client','order_status','status','delivery','comment','group_image',)


