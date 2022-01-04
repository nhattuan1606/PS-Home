from django.contrib import admin
from .models import InforUser


class InforUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'time', 'monney', 'is_locked', 'note')


# Register your models here.
admin.site.register(InforUser, InforUserAdmin)
