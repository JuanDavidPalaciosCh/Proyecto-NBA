import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NBA_project.settings')
django.setup()
 
import datetime
import time
import requests
from equipos_info.models import Jugador


url = "https://api-nba-v1.p.rapidapi.com/players"

headers = {
    "X-RapidAPI-Key": "c1d97fa4dbmshd7217d7e021e446p147efcjsn6097dc6a513a",
    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")

n = 41 # Limite equipos NBA (40)

for i in range(n):

    response = requests.request("GET", url, headers=headers, params={"team": i + 1, "season" : year})
    response_json: dict = response.json()

    players = response_json["response"]

    for j in range(len(players)):

        try:

            a = Jugador(
                team_id=(i + 1),
                name=players[j]["firstname"],
                lastname=players[j]["lastname"],
                position=players[j]["leagues"]["standard"]["pos"],
                number=players[j]["leagues"]["standard"]["jersey"]
            )

        except:
             a = Jugador(
                team_id=(i + 1),
                name=players[j]["firstname"],
                lastname=players[j]["lastname"],
                position='N/A'
            )

        a.save()

        print(a.team_id)

    time.sleep(10)
