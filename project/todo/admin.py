from django.contrib import admin

from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    actions = ("archive",)

    def archive(self, request, queryset):
        for todo in queryset:
            todo.archive()


admin.site.register(ToDo, ToDoAdmin)
