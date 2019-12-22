from django.contrib import admin
from .models import Subject, Course, Module
# Register your models here.

# register subject in the admin
@admin.register(Subject)
# contents information of the course to show admin
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
# to add module
class ModuleInline(admin.StackedInline):
    model = Module

# register admin for course 
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
