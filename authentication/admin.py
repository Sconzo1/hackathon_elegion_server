from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserRank, UserType, User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_superuser', 'birthdate')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Инфо', {'fields': ('surname', 'name', 'datetime')}),
        ('Права', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Данные', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'id_user_type', 'id_user_rank')}
         ),
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
        ('Инфо', {
            'classes': ('wide',),
            'fields': ('surname', 'name', 'datetime')}),
        ('Права', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserType)
admin.site.register(UserRank)
