import csv
from locations.models import Film, Location, Director, Link, Coordinate

with open('locations/Interactive_Map_Data.csv',errors='replace') as shit:
    shit_eater = csv.reader(shit,delimiter=',')
    next(shit_eater)
    next(shit_eater)
    for crap in shit_eater:
        # this is going to be tough
        # create Coordinates
        coordinate = Coordinate.objects.create(
            latitude=crap[9],
            longitude=crap[10]
        )
        # get or create location
        location, created = Location.objects.get_or_create(
            borough=crap[11],
            neighborhood=crap[12],
            description=crap[8],
        )
        # set relationship (Coordinates and Locations)
        location.coordinate = [coordinate]
        # if Film.objects.filter(title=crap[0]):
        #     continue
        movie_link = Link.objects.create(link=crap[15])
        film, created = Film.objects.get_or_create(
            title=crap[0],
            link=movie_link,
            year=crap[1]
        )
        film.location = [location]
        # get or create director url
        links = crap[7].split(',')
        # Fuck movies have multiple directors
        directors = crap[6].split(',') 

        if len(links)==len(directors):
            for i in range(len(links)):
                link, created = Link.objects.get_or_create(link=links[i])
                director,created = Director.objects.get_or_create(
                    link=link,
                    name=directors[i]
                )
                film.director.add(director)
        else:
            print(directors,links)
            raise NameError("Director/Link Mismatch")
        
