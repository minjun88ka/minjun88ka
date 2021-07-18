from django.contrib import admin
from .models import Dsuser

class DsuserAdmin(admin.ModelAdmin):
    list_display = ('id', 'password')

admin.site.register(Dsuser, DsuserAdmin)
