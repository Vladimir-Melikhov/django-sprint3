from django.contrib import admin

from .const import TEXT_NUM
from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'short_text',
        'pub_date',
        'category',
        'author'
    )

    def short_text(self, obj):
        """Возвращает укороченную строку."""
        return obj.text[:TEXT_NUM] + '...' if len(
            obj.text
        ) > TEXT_NUM else obj.text


admin.site.register(Post, PostAdmin)
admin.site.register(Location)
admin.site.register(Category)
