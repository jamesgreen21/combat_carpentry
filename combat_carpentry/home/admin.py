from django.contrib import admin
from .models import Post, Service


admin.site.register([Post, Service])
