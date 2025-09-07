from django.contrib import admin
from .models import Contact

# Register your models here.

class FormatContacts(admin.ModelAdmin):
    list_display = ("name", "email","message","attachment")
admin.site.register(Contact,FormatContacts)