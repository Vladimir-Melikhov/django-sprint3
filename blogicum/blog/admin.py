from django.contrib import admin

from .const import TEXTNUM
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
        """Возвращает первые 60 символов поля text."""
        return obj.text[:TEXTNUM] + '...' if len(obj.text) > TEXTNUM else obj.text



admin.site.register(Post, PostAdmin)
admin.site.register(Location)
admin.site.register(Category)
