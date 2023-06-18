from django.contrib import admin
from .models import *

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display=["id","filmismi","kategori"]
    list_display_links=["id"]
    list_filter=["kategori"]
    search_fields=["filmismi","kategori__name"]
    list_per_page=2
    list_editable=["filmismi"]



admin.site.register(Movies,MovieAdmin)
admin.site.register(Tur)
admin.site.register(Kategori)
admin.site.register(Izlenen)
