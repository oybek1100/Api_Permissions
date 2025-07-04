from django.contrib import admin
from .models import Subject , Course , CustomUser
from django.contrib.auth.models import Group




class AdminRegisterSubject(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Subject, AdminRegisterSubject)
admin.site.register(Course)
admin.site.register(CustomUser)
admin.site.unregister(Group)
