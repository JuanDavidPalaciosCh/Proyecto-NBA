from django.shortcuts import render
from NBA_stats.models import Equipo
from equipos_info.models import Jugador
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError


#@login_required
def equipos_info(request):
    try:
        team_id = set_id(request)

    except MultiValueDictKeyError:    
        team_id = 0

    team = Equipo.objects.get(id_equipo=team_id)

    jugadores = Jugador.objects.filter(team_id=team_id+1)

    jugadores = jugadores.order_by('number')

    context = {'equipo' : team, 'team_id' : team_id, 'jugadores' : jugadores}

    return render(request, 'equipos_info/equipos_info.html', context)


def set_id(request):
    team_id = int(request.GET["team_id"])

    if team_id < 0:
        team_id = 40
    
    elif team_id > 40:
        team_id = 0

    return team_id