from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Landmark)
admin.site.register(Image)
