from django.contrib import admin
from .models import Author, BookCategory, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publish_year', 'publication_name', 'for_class')
    search_fields = ('title', 'author__name')
    list_filter = ('category', 'for_class')
