from django.forms import ModelForm
from .models import Todo, Screen, Macro, Device, Task, Help

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
        fields = ['name', 'command', 'termination']

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'ip', 'port']

class HelpForm(ModelForm):
    class Meta:
        model = Help
        fields = ['title', 'info', 'user']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'version', 'modified', 'macro_name', 'device', 'type', 'message']