from django.contrib import admin
from .models import (
    Blog,
    Comment
)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    prepopulated_fields = {
        'slug': ('title',),
    }


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)