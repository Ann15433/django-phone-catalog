from django.contrib import admin
from .models import Phone  

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    exclude = ['release_date']

    list_display = ['name', 'price', 'image_preview']
    search_fields = ['name']  

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50"/>'
        return "Нет изображения"
    image_preview.allow_tags = True
