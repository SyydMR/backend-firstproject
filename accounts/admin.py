from django.contrib import admin
from accounts.models import CustomUser
# Register your models here.
# @admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    # date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id', 'first_name', 'last_name', 'username', 'is_active', 'is_staff', )
    list_filter = ('is_active', 'is_staff', )
    # ordering = ['created_date']
    # or ordering = ['-created_date']

admin.site.register(CustomUser, UserAdmin)