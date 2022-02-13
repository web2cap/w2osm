# from django.contrib import admin
from django.contrib.gis import admin

from .models import WorldBorder


class WorldBorderAdmin(admin.OSMGeoAdmin):
    # list_display = ("pk", "text", "created", "author", "post")
    search_fields = ("name",)
    # list_filter = ("created",)


admin.site.register(WorldBorder, WorldBorderAdmin)


# admin.site.register(Comment, CommentAdmin)
