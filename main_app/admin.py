from django.contrib import admin

# Register your models here.

from .models import Game, Store

admin.site.register(Game)
admin.site.register(Store)
