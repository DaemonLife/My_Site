from django.contrib import admin

# Register your models here.
from .models import Bb

class BbAdmin(admin.ModelAdmin):
    # * отображение столбцов в таблице 
    list_display = ('title', 'content', 'price', 'published')
    # * гиперссылки для отображенных столбцов
    list_display_links = ('title', 'content')
    # * по каким полям ведется поиск
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)