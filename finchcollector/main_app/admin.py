from django.contrib import admin

# Register your models here.
from django.contrib import admin
# add Feeding to the import
from .models import Finch, Feeding

admin.site.register(Finch)
# register the new Feeding Model 
admin.site.register(Feeding)