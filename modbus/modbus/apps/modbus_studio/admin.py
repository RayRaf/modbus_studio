from django.contrib import admin
from .models import Device, MBS_device_type, MBS_param_name, MBS_param_value, MBS_project, MBS_system

# Register your models here.
# admin.site.register(Device)
admin.site.register(MBS_system)
admin.site.register(MBS_project)
admin.site.register(MBS_device_type)
admin.site.register(MBS_param_name)
admin.site.register(MBS_param_value)