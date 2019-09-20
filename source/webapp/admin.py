from django.contrib import admin
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'description', 'status', 'date_perf']
    list_filter = ['status']
    list_display_links = ['pk', 'description']
    search_fields = ['status', 'date_perf']
    fields = ['description', 'status', 'date_perf']


admin.site.register(Task, TaskAdmin)
