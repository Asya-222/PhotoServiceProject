from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ungettext_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.admin import GenericTabularInline
from django.forms import ModelForm, PasswordInput
from django.contrib import admin

from client.models import (
     Client,
     Size,
     City,
     Addresses,
     Image,
     Order,
     OrderStatus,
     ImageGroup,
     CrudOrder

)

def image_tag(self):
    from django.utils.html import escape
    return u'<img src="%s" />'
image_tag.short_description = 'Image'
image_tag.allow_tags = True




class ClientAdmin(admin.TabularInline):
    model = Client

class ImageAdmin(admin.ModelAdmin):
    model = Image
    fields = ('image_tag', 'path')
    readonly_fields = ('image_tag',)

class OrderStatusAdmin(admin.TabularInline):
    model = OrderStatus
    extra = 0

class ImageGroupAdmin(admin.TabularInline):
    model = ImageGroup
    list_display = ['images','size','order','quantity']
    readonly_fields = ['images','size','order','quantity']
    inlines = [ImageAdmin,]
    extra = 0



class ImageGroupCrudAdmin(admin.TabularInline):
    model = ImageGroup
    list_display = ['images','size','order','quantity']
    inlines = [ImageAdmin,]
    extra = 0


class OrderAdmin(admin.ModelAdmin):

    inlines = [ ImageGroupAdmin]

    readonly_fields = ('client_phone','client','address','benefit','city')
    
    change_form_template = 'admin/custom/change_form.html'
    list_display = ('id','client','order_status','client_phone','client','address','benefit','city')
    def has_add_permission(self, request, obj=None):
        return False
    class Media:

        css = {
            'all': (
                'css/admin.css',
            )
        }

    def client_phone(self, obj):
        return obj.client.phone_number
    
    def benefit(self, obj):
        return obj.address.benefit
    
    def city(self, obj):
        return obj.address.city.name



class CrudOrderAdmin(admin.ModelAdmin):

    model = CrudOrder
    inlines = [ ImageGroupCrudAdmin]

    
    list_display = ('id','client','order_status','client','address')



class ImageGroupAdmin(admin.ModelAdmin):
    model = ImageGroup


class MyEmsAdminSite(AdminSite):

    site_title = 'Annaniks LLC'
    #
    site_header = 'Annaniks LLC'
    #
    index_title = 'Annaniks LLC'

class UserForm(ModelForm):
    print('hop')

    class Meta:
        model = User
        fields = "__all__"
        # widgets = {
        #     'password': PasswordInput(),
        # }

    def save(self, commit=True):
        print(self.instance._state.adding, 'mtav')
        # Save the provided password in hashed format
        if self.instance._state.adding:
            user = super(UserForm, self).save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user
        else:
            user = super(UserForm, self).save(commit=False)
            if commit:
                user.save()
            return user

class UserAdmin(admin.ModelAdmin):
    form = UserForm

myems_admin_site = MyEmsAdminSite()
myems_admin_site.register(User, UserAdmin)
myems_admin_site.register(Group)
myems_admin_site.register(Client)
myems_admin_site.register(Size)
myems_admin_site.register(City)
myems_admin_site.register(Addresses)
myems_admin_site.register(Image,ImageAdmin)
myems_admin_site.register(Order,OrderAdmin)
myems_admin_site.register(CrudOrder,CrudOrderAdmin)

myems_admin_site.register(OrderStatus)
myems_admin_site.register(ImageGroup,ImageGroupAdmin)

