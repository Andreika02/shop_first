from django.contrib import admin
from Core.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    list_editable = ("email",)

