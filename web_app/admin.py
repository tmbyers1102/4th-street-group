from django.contrib import admin
from .models import Project, Screengrab, Requirement, Contact

class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'progress'
    )

    def screengrab_info(self, obj):
        return obj.description


admin.site.register(Project, ProjectInfoAdmin),


class ScreengrabInfoAdmin(admin.ModelAdmin):
    list_display = (
        'screen_grab',
        'assigned_project'
    )

    def screengrab_info(self, obj):
        return obj.description


admin.site.register(Screengrab, ScreengrabInfoAdmin)


class RequirementInfoAdmin(admin.ModelAdmin):
    list_display = (
        'requirement_title',
        'assigned_project'
    )

    def requirement_info(self, obj):
        return obj.description


admin.site.register(Requirement, RequirementInfoAdmin)
admin.site.register(Contact)