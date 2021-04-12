from django.contrib import admin
from .models import Todo, Screen, Macro, Device

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)


class ScreenAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Screen, ScreenAdmin)


admin.site.register(Macro)
admin.site.register(Device)
# Register your models here.