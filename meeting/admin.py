from django.contrib import admin
from .models import Meeting

class ListMeeting(admin.ModelAdmin):
    list_display = ('title', 'collaborator','datetime','details','url_meeting')

admin.site.register(Meeting, ListMeeting)