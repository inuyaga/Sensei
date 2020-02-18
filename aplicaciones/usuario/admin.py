from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from aplicaciones.usuario.models import User

class AdminUser(UserAdmin):
    list_display = (
        'username', 
        'first_name', 
        'last_name', 
        'email', 
        'is_alumno', 
        'is_maestro', 
        'fecha_nacimiento', 
        )
    list_filter = (
        'is_alumno',
        'is_maestro',
        'email',
        'username',
        'is_superuser',
    )
admin.site.register(User, AdminUser)