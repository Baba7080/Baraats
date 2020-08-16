from django.contrib import admin


from .models import ServiceNeed
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class ServiceAdmin(ModelAdmin):
    list_display = ['city']
    search_fields = ['Phone_no','city']
    list_filter =['city','Phone_no']
admin.site.register(ServiceNeed,ServiceAdmin)