from django.contrib import admin

# Register your models here.
from projects.models import Image, Project, Location


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
