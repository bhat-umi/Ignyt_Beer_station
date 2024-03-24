from django.contrib import admin

# Register your models here.
from .models import Order

# Register MyModel with the admin site
@admin.register(Order)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'total','items','timestamp']