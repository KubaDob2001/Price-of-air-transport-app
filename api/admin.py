from django.contrib import admin

from .models import AirPlane, AirPort

admin.site.register(AirPort)
admin.site.register(AirPlane)
