from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'priority', 'created_at', 'status', 'due_date')
    search_fields = ['title', 'desc']
    list_filter = ('priority', 'status', 'due_date')
    ordering = ('-created_at', 'priority', 'status', 'due_date')

admin.site.register(Task, TaskAdmin)

