from django.contrib import admin
from .models import Strain

# Register your models here.

class StrainModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp', 'user', 'strain_type']
    class Meta:
        model = Strain

admin.site.register(Strain, StrainModelAdmin)