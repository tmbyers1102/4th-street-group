from django.contrib import admin
from .models import Project, Requirement, Screengrab, Contact, Log, Tech

class LogInfoAdmin(admin.ModelAdmin):
    list_display = (
        'project',
        'title'
    )

    def log_info(self, obj):
        return obj.description


admin.site.register(Log, LogInfoAdmin),

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


admin.site.register(Contact)
admin.site.register(Tech)
admin.site.register(Requirement)