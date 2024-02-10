from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'Fname','Lname', 'is_admin')
    list_filter = ('is_admin',) 
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('Fname',)}),
        ('Personal Info', {'fields': ('Lname',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = ( 
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'Fname','Lname', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()

admin.site.register(User, UserModelAdmin)


