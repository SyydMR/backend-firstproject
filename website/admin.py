from django.contrib import admin
from website.models import Destination, Comment, Destination_User, Invoice, Transportation, Corporation, City, Country  
# Register your models here.
# @admin.register(Post)
class DestinationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id', 'city_id' ,'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status', )
    ordering = ['created_date']
    # or ordering = ['-created_date']
    search_fields = ['description']

class DesignAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id', 'name', 'created_date')
    ordering = ['created_date']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id', 'title', 'ref_id' , 'created_date')
    ordering = ['created_date']



admin.site.register(Destination, DestinationAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Destination_User)
admin.site.register(Invoice)
admin.site.register(Transportation, DesignAdmin)
admin.site.register(Corporation, DesignAdmin)
admin.site.register(City, DesignAdmin)
admin.site.register(Country, DesignAdmin)


