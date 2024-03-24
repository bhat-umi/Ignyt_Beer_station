from django.contrib import admin

# Register your models here.
from .models import Reservations

# Register MyModel with the admin site
@admin.register(Reservations)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone','email','date','description']