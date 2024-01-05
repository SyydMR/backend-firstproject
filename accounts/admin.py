from django.contrib import admin
from accounts.models import User

# Register your models here.
@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff']
    search_fields = ['username', 'email']