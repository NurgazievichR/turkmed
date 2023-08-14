from django.contrib import admin

from apps.news.models import New, License, Gallery

admin.site.register(New)
admin.site.register(License)
admin.site.register(Gallery)


