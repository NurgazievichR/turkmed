from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.safestring import mark_safe

from apps.doctors.models import Doctor, Award

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Doctor)

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('display_image','title')

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="400" height="500" />')
        return "No Image"
    display_image.short_description = 'Image'


    
