from django.contrib import admin
from .models import Todo, Screen, Macro, Device, Task, Help


admin.site.site_header = 'Autonomica Admin'

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ['title', 'important', 'created']

admin.site.register(Todo, TodoAdmin)


class ScreenAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ['title', 'location', 'created', 'enabled']


class HelpAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ['title', 'user', 'created']

admin.site.register(Help, HelpAdmin)

admin.site.register(Screen, ScreenAdmin)


admin.site.register(Macro)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip', 'port', 'cinema', 'tasker']


admin.site.register(Device, DeviceAdmin)


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('modified',)
    list_display = ['screen', 'task_name', 'device', 'type', 'message']

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    # def has_delete_permission(self, request, obj=None):
    #     return False

admin.site.register(Task, TaskAdmin)
# Register your models here.


