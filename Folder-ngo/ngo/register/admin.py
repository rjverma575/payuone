from django.contrib import admin
from .models import UserRegister
# Register your models here.
@admin.register(UserRegister)
class UserRegisterAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'phone', 'message')

