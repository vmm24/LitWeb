from django.contrib import admin

# Register your models here.
from .models import Events

class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    search_fields = ['title', 'content']
    prepopulated_fields = {'content': ('title',)}
  
admin.site.register(Events, EventsAdmin)
