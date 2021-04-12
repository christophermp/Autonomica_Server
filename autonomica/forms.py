from django.forms import ModelForm
from .models import Todo, Screen, Macro, Device

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']

class ScreenForm(ModelForm):
    class Meta:
        model = Screen
        fields = ['title', 'location', 'enabled']

class MacroForm(ModelForm):
    class Meta:
        model = Macro
        fields = ['name', 'command', 'ip', 'termination']

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'ip', 'port']