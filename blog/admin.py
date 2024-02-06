from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = "__all__"


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title', 'cat', 'time_created', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'time_created')
    list_editable = ('is_published',)
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_created',
              'time_update')
    readonly_fields = ('get_html_photo', 'time_created', 'time_update')
    save_on_top = True

    def get_html_photo(self, objects):
        if objects.photo:
            return mark_safe(f"<img src='{objects.photo.url}' width='50'>")

    get_html_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = "Админ-панель"
admin.site.site_header = "Админ-панель"
