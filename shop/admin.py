from django.contrib import admin

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class AdditionalImagesInline(admin.TabularInline):
    model = models.AdditionalProductImage


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'discount',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available', 'price', 'discount']
    inlines = [AdditionalImagesInline]
    prepopulated_fields = {'slug': ('name',)}


