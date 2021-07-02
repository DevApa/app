from django.contrib import admin
from core.erp.models import *

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('names', 'dni', 'date_joined')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'file', 'pvp')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('names', 'surnames', 'dni', 'birthday', 'address', 'sex')