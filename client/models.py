from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name='user_client', null=True)
    google_id = models.TextField(null=True)
    facebook_id = models.TextField(null=True)
    instagram_id = models.TextField(null=True)
    vk_id = models.TextField(null=True)
    email_validation_token = models.TextField(null=True)
    device_token = models.TextField(null=True)
    device_os = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    target_wight = models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    delivery_price = models.IntegerField()

    def __str__(self):
        return self.name


class Addresses(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)
    benefit = models.CharField(max_length=1000)
    city = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.address

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.ImageField()

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.address

class OrderStatus(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)

    def __str__(self):
        return ' '

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    ratio = models.DecimalField(max_digits=10, decimal_places=5)
    price = models.IntegerField()

    def __str__(self):
        return self.label

class ImageGroup(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus,on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    delivery = models.BooleanField()
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.comment