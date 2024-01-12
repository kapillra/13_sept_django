from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'Demo Django'
admin.site.register(Master)