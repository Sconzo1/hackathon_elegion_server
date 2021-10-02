from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserRank, UserType, User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff',)
    list_filter = ('email', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Инфо', {'fields': ('first_name', 'last_name', 'email')}),
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
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserType)
admin.site.register(UserRank)
