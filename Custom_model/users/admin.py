from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    list_display = ['username', 'email', 'phone']


admin.site.register(CustomUser, CustomUserAdmin)
