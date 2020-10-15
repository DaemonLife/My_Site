from django.contrib import admin

# Register your models here.
from .models import Bb, Rubric

# ! this is for display in admin panel
class BbAdmin(admin.ModelAdmin):
    # * отображение столбцов в таблице 
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    # * гиперссылки для отображенных столбцов
    list_display_links = ('title', 'content')
    # * по каким полям ведется поиск
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)