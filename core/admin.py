from django.contrib import admin

# Register your models here.

from .models import Visits, Workspaces

@admin.register(Workspaces)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kind', 'description')

@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
    list_display = ('dataField', 'yearField', 'monthField', 'dayOfMonth', 'dayOfWeek', 'workspace')