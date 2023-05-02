from django.contrib import admin

# Register your models here.
#root/root username/password = superuser
from django.utils.safestring import mark_safe

from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','get_html_photo','is_published','price','old_price')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')
    prepopulated_fields = {'slug':('title',)}
    fields = (
    'title', 'slug', 'cat', 'content', 'photo', 'get_html_photo2',
    'is_published', 'time_create', 'time_update','price','old_price')

    readonly_fields = ('time_create', 'time_update', 'get_html_photo2')
    save_on_top = True


    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f'<img src={object.photo.url} width=50>')
        else:
            return "Нет фото"
    get_html_photo.short_description='Фото'

    def get_html_photo2(self,object):
        if object.photo:
            return mark_safe(f'<img src={object.photo.url} width=150>')
        else:
            return "Нет фото"
    get_html_photo2.short_description='Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {"slug":('name',)}

admin.site.register(Women,WomenAdmin)
admin.site.register(Category,CategoryAdmin)


admin.site.site_title= 'Админка'
admin.site.site_header= 'Админка'
