from django.contrib import admin

from women.models import Women, Category

class WomenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Women._meta.fields]
admin.site.register(Women)
admin.site.register(Category)