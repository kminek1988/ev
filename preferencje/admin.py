from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Region, Miasto, Rodzaj
# Register your models here.


class RegionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Region, RegionAdmin)


class MiastoAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Miasto, MiastoAdmin)


class RodzajAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Rodzaj, RodzajAdmin)
