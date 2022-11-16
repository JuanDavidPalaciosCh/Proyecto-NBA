from django.contrib import admin
from .models import Jugador


class JugadorAdmin(admin.ModelAdmin):
    
        list_display = ('name', 'lastname', 'position', 'number', 'team_id')
    
        search_fields = ('name', 'lastname', 'position', 'number', 'team_id')
    
        ordering = ('name', 'lastname', 'position', 'number', 'team_id')


admin.site.register(Jugador, JugadorAdmin)