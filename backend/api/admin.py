from django.contrib import admin
from .models import TodoTable


class TodoAdmin(admin.ModelAdmin):  # add this
  list_display = ('id', 'text', 'completed')  # add this
# Register your models here.
admin.site.register(TodoTable, TodoAdmin)