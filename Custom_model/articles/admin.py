from django.contrib import admin

from .models import Articles
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserCreationForm
#     list_display = ['username', 'email', 'phone']


admin.site.register(Articles)