from django.contrib import admin

# Register your models here.
from .models import Player, FavouritePlayer

admin.site.register(Player)
admin.site.register(FavouritePlayer)