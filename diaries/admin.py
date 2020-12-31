from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(poems)
admin.site.register(shayri)
admin.site.register(oneliners)
