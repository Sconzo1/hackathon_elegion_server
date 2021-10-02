from django.contrib import admin
from django.utils.html import format_html

from .models import Task, UserTask, ChatType, ForeignChat


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


class ChatTypeAdmin(admin.ModelAdmin):
    model = ChatType
    list_display = ('name',)
    fieldsets = (
        (None, {'fields': ('name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name',)}
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


class ForeignChatAdmin(admin.ModelAdmin):
    model = ForeignChat
    list_display = ('name', 'telegram', 'id_type')
    list_filter = ('id_type',)
    fieldsets = (
        (None, {'fields': ('name', 'tg_link', 'id_type',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'tg_link', 'id_type',)}
         ),
    )
    search_fields = ('name', 'tg_link', 'id_type')
    ordering = ('name',)

    def telegram(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.tg_link)


admin.site.register(Task, TaskAdmin)
admin.site.register(UserTask, UserTaskAdmin)
admin.site.register(ChatType, ChatTypeAdmin)
admin.site.register(ForeignChat, ForeignChatAdmin)
