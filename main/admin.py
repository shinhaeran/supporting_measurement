from django.contrib import admin
from .models import CustomUser,Data,Cart
from django.contrib.auth.admin import UserAdmin
from .forms import CreateUserForm,UserChangeForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CreateUserForm
    form = UserChangeForm
    model = CustomUser
    list_display = ["group", "username",'area1','area2']

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Data)
admin.site.register(Cart)
