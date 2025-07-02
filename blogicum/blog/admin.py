from django.contrib import admin

from .models import Post, Location, Category


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'short_text',
        'pub_date',
        'category',
        'author'
    )

    def short_text(self, obj):
        """Возвращает первые 20 символов поля text."""
        return obj.text[:60] + '...' if len(obj.text) > 60 else obj.text


admin.site.register(Post, PostAdmin)
admin.site.register(Location)
admin.site.register(Category)
