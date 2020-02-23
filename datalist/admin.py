from django.contrib import admin
from .models import Datalist

class DatalistAdmin(admin.ModelAdmin):
    # list_display=("name", "cardnumber")
    list_display = ("name", "city", "cardnumber", "phonenumber", "created", "token")

# Register your models here.
admin.site.register(Datalist, DatalistAdmin)