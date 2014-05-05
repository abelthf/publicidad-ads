from django.contrib import admin
from ads.models import Categoria, Elemento
# Register your models here.
# register your .


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    prepopulated_fields = {"slug": ("nombre",)}


class ElementoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'seccion', 'publicado_en']
    list_filter = ['categoria', 'publicado_en']


admin.site.register(Elemento, ElementoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
