from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active', )
    list_display_links = ('first_name', 'last_name',)
    readonly_fields = ('last_login', 'date_joined',) # поля только для чтения
    ordering = ('-date_joined',)


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)