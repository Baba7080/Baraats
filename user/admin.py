from django.contrib import admin
from user.models import Contact
from user.models import Service
from user.models import Profile
from user.models import Post
from user.models import Cotegories
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class ContactAdmin(ModelAdmin):
    list_display = ['first_name']
    search_fields = ['first_name','city']
    list_filter =['city']
admin.site.register(Contact,ContactAdmin),
admin.site.register(Service),
admin.site.register(Post),
admin.site.register(Profile),
admin.site.register(Cotegories)