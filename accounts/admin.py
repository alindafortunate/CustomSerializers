from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomAdmin(UserAdmin):
    list_display = ["first_name", "last_name", "email", "is_staff"]


admin.site.register(CustomUser, CustomAdmin)
