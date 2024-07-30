from django.contrib import admin

from .models import Record, Image, Medicine


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    pass
