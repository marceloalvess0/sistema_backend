from django.contrib import admin
from .models import Pdi

class ListPdi(admin.ModelAdmin):
    list_display = ('objective_title','developed_areas','initial_datetime','final_datetime','reference_url','file','description')

admin.site.register(Pdi, ListPdi)
