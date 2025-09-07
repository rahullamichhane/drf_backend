from django.contrib import admin
from .models import Note

class FormatNotes(admin.ModelAdmin):
    list_display = ("tittle","created_at","author")
    list_per_page = 10
admin.site.register(Note,FormatNotes)
    
    

    
    
