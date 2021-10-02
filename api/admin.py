from django.contrib import admin

from .models import Task, UserTask


class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('name', 'desc')
    fieldsets = (
        (None, {'fields': ('name', 'desc',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'desc',)}
         ),
    )
    search_fields = ('name',)
    ordering = ('name',)


class UserTaskAdmin(admin.ModelAdmin):
    model = UserTask
    list_display = ('id_user', 'id_task', 'id_manager', 'date_expired', 'is_done', 'weight')
    list_filter = ('id_user', 'id_task', 'id_manager', 'date_expired', 'is_done', 'weight')
    fieldsets = (
        (None, {'fields': ('id_user', 'id_task', 'id_manager', 'date_expired', 'is_done', 'date_done', 'weight',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_user', 'id_task', 'id_manager', 'date_expired', 'weight',)}
         ),
    )
    search_fields = ('id_user', 'id_task', 'id_manager')
    ordering = ('id_user', 'date_expired', '-weight')


admin.site.register(Task, TaskAdmin)
admin.site.register(UserTask, UserTaskAdmin)
