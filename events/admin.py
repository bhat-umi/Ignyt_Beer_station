from django.contrib import admin

# Register your models here.

from .models import Registrations

# Register MyModel with the admin site
@admin.register(Registrations)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
