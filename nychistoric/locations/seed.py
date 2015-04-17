import csv
from locations.models import Film, Location, Director

with open('locations/Interactive_Map_Data.csv',errors='replace') as shit:
    shit_eater = csv.reader(shit,delimiter=',')
    next(shit_eater)
    next(shit_eater)
    for crap in shit_eater:
        location = Location.objects.create(
            borough=crap[11],
            neighborhood=crap[12],
            description=crap[8],
            latitude=crap[9],
            longitude=crap[10]
        )

        director = Director.objects.create(
            name=crap[6],
            link=crap[7]
        )
        film = Film.objects.create(
            title=crap[0],
            link=crap[15],
            year=crap[1],
            director=director,
            location=location
        )