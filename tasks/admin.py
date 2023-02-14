from django.contrib import admin

from .models import *

@admin.register(TaskModel)
class TaskModel_admin(admin.ModelAdmin):
    ...