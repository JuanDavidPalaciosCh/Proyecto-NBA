from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from calendario_juegos.get_games import get_games
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator
from NBA_stats.models import Equipo
from datetime import date


@login_required
def calendario_juegos(request):

    equipos = Equipo.objects.order_by('nombre')

    previous_date = str(date.today())

    try:
        fecha = set_date(request)
        juegos = get_games({"date": fecha})
        fecha = "{}-{}-{}".format(fecha[:4], fecha[5:7], fecha[8:])

    except MultiValueDictKeyError:
        juegos = get_games({"date": previous_date}) #Consulta api para obtener juegos dia de hoy.
    
        fecha = previous_date
        fecha = "{}-{}-{}".format(fecha[:4], fecha[5:7], fecha[8:])

    # pagination
    p = Paginator(juegos, 3)
    page = request.GET.get('page')
    juegos = p.get_page(page)

    context = {"juegos" : juegos, "equipos" : equipos, "fecha_hoy": fecha}

    return render(request, 'calendario_juegos/calendario.html', context) 


def set_date(request):
    date = str(request.GET["date"])

    return date
