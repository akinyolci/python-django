from django.contrib import admin

# Register your models here.

from .models import Pet

@admin.register(Pet)
class Petadmin(admin.ModelAdmin):
    pass

