from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
from NBA_stats.models import Equipo
from NBA_stats.get_team_stats import get_stats
from NBA_stats.get_winner import eval_winner
from django.views.generic import TemplateView


@login_required
def home(request):
    equipos = Equipo.objects.order_by('nombre')
    context = {'equipos' : equipos, 'id_equipo_1' : 0, 'id_equipo_2' : 40}
    return render(request, 'NBA_stats/home.html', context)

 
@login_required
def team_vs_team(request):
    home = int(request.GET["home"])
    visitor = int(request.GET["visitor"])
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    
    home_img = "/static/images/logos/imagen_equipo_" + str(home) + ".png"
    visitor_img = "/static/images/logos/imagen_equipo_" + str(visitor) + ".png"

    home_name = Equipo.objects.get(id_equipo=home).nombre
    visitor_name = Equipo.objects.get(id_equipo=visitor).nombre

    # Obtener estadisticas de equipo
    home_stats = get_stats({"id":home + 1, "season":year})
    visitor_stats = get_stats({"id":visitor + 1, "season":year})

    winner_home, home_percentage, visitor_percentage = eval_winner(home_stats, visitor_stats)

    if winner_home != None:
        if winner_home:
            winner = home
        else:
            winner = visitor

    else:
        winner = -1

    context = {
        "home_img": home_img, "visitor_img": visitor_img, "home_name": home_name, "visitor_name": visitor_name,
        "home_stats": home_stats, "visitor_stats": visitor_stats, "winner": winner,
        "home_percentage": "{:.2f}".format(home_percentage), "visitor_percentage": "{:.2f}".format(visitor_percentage)
     }

    return render(request, 'NBA_stats/TeamVsTeam.html', context)


def cerrar_sesion(request):
    logout(request)
    return redirect('/')


class Error404View(TemplateView):
    template_name = 'NBA_stats/404.html'


class Error500View(TemplateView):
    template_name = 'NBA_stats/500.html'

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view