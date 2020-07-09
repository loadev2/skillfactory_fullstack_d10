from django.contrib import admin
from common.models import Brand, Model, Car
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass