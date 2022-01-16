from django.contrib import admin
from desafio.models import Region, Fruit



class Regions(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ['name']


class Fruits(admin.ModelAdmin):
    list_display = ["name",'region_name']
    list_display_links = ["name",'region_name']
    search_fields = ['name','region_name']


admin.site.register(Region,Regions)
admin.site.register(Fruit,Fruits)