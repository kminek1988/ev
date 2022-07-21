from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Formularz
class FormularzAdmin(admin.ModelAdmin, ExportActionMixin):
    pass


admin.site.register(Formularz, FormularzAdmin)
# Register your models here.
