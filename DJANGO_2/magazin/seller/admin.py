from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create', )
    prepopulated_fields = {"slug": ("title", )}
    fields = ('title', 'slug', 'content', 'code', 'img1', 'img2', 'img3', 'img4', 'img5', 'time_create')
    readonly_fields = ('time_create', )
    save_on_top = True

    def get_html_photo(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=50>")


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы к фильму"""
    list_display = ("name", "review", 'time_create', )

admin.site.register(RatingStar)
admin.site.register(Project, ProjectAdmin)
