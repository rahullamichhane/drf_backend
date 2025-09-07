from django.contrib import admin
from .models import Student, ClassCategory

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'class_category', 'parent_name', 'address')
    search_fields = ('name', 'student_id')

@admin.register(ClassCategory)
class ClassCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register your models here.
