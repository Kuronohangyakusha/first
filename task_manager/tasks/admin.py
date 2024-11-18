from django.contrib import admin

# Register your models here.
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('tache','description','status','datedecreation','date_echeance')

    list_filter = ('status',)

    search_fields = ('tache','description')


admin.site.register(Task,TaskAdmin)