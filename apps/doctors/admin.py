from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.doctors.models import Doctor, Award

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Doctor)

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image')

    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'

    
