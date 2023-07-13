from django.contrib import admin
from  . import models

# Register your models here.


class DetectAdmin(admin.ModelAdmin):
    list_display= (['ifile'])
admin.site.register(models.Detect,DetectAdmin)
