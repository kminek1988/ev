from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Profil

# Register your models here.
class ProfilAdmin(admin.ModelAdmin, ExportActionMixin):
    pass
admin.site.register(Profil, ProfilAdmin)