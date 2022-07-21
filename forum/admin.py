from django.contrib import admin
from .models import Room, Message
from import_export.admin import ExportActionMixin
# Register your models here.


admin.site.register(Room)
admin.site.register(Message)
