from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserRank, UserType, User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('surname', 'name', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'birthdate')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Инфо', {'fields': ('surname', 'name', 'birthdate')}),
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
            'fields': ('email', 'password1', 'password2'), }),
        ('Инфо', {
            'classes': ('wide',),
            'fields': ('surname', 'name', 'birthdate')}),
        ('Права', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    readonly_fields = ('last_login',)
    search_fields = ('email', 'name', 'surname')
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserType)
admin.site.register(UserRank)
