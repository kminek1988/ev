from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Event


class EventAdmin(admin.ModelAdmin, ExportActionMixin):
    list_display = ('name', 'region', 'miasto', 'rodzaj', 'start', 'end', )


admin.site.register(Event, EventAdmin)
