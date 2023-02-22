from django.contrib import admin

from api.models import Rover, Planet, Obstacle


admin.site.register(Planet)
admin.site.register(Rover)
admin.site.register(Obstacle)