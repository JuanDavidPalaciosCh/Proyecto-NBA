"""NBA_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.conf import settings

from NBA_stats.views import home, team_vs_team, cerrar_sesion, Error404View, Error500View
from calendario_juegos.views import calendario_juegos
from equipos_info.views import equipos_info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', cerrar_sesion, name='logout'),
    path('calendario/', calendario_juegos, name='calendario'),
    path('teamvsteam/', team_vs_team, name='teamvsteam'),
    path('equipos_info/', equipos_info, name='equipos_info'),
]

handler404 = Error404View.as_view()
handler500 = Error500View.as_error_view()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
