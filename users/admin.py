from django.contrib import admin
from django.contrib.auth.models import  User
# Register your models here.
from .models import EmpTable
class EmpAdmin(admin.ModelAdmin):
	list_display = ('empEmail','empName')

admin.site.register(EmpTable,EmpAdmin)
admin.site.unregister(User)
#admin.site.register(User, UserAdmin)