from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ungettext_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

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
     ImageGroup

)

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
myems_admin_site.register(Image)
myems_admin_site.register(Order)
myems_admin_site.register(OrderStatus)
myems_admin_site.register(ImageGroup)
