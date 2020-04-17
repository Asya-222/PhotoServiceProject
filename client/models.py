from django.db import models
from django.contrib.auth.models import User
import  os
from django.utils.safestring import mark_safe
from django.conf import settings

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
        return str(self.address)

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.ImageField()

    def __str__(self):
        return str(self.path.url)


    def url(self):
        # returns a URL for either internal stored or external image url

            # is this the best way to do this??
            return os.path.join('/', settings.MEDIA_URL, os.path.basename(str(self.path)))

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))

class OrderStatus(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)

    def __str__(self):
        return str(self.label)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.ForeignKey(Addresses,null=True,blank=True,on_delete=models.CASCADE)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus,null=True,blank=True,on_delete=models.CASCADE)
    delivery = models.BooleanField(null=True,blank=True)
    comment = models.CharField(null=True,blank=True,max_length=1000)
    class Meta:
        permissions = (
            ('read_item','Can read item'),
        )
    def __str__(self):
        return str(self.id)

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
    images = models.ManyToManyField(Image)

    def screenshots_as_list(self):
        return self.images.split('\n')

class CrudOrder(Order):

    class Meta:
        verbose_name = "զակազ թեստ"
        
        # nullslast = True

        proxy=True