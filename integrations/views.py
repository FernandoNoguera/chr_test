import requests
from django.shortcuts import render
from integrations.models import (Station,Response, Location,Extra)
import datetime
from django.utils import timezone

def index(request):
    list_stations = list()
    # Realizar la solicitud GET a la API
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    data = response.json()
    # Crear una instancia de los modelos y guardarla en la base de datos
    try:
        location = Location.objects.get(city=data['network']['location']['city'])
    except:
        location = Location(
            city=data['network']['location']['city'],
            country = data['network']['location']['country'],
            latitude = data['network']['location']['latitude'],
            longitude = data['network']['location']['longitude'],
        )
        location.save()
    for station in data['network']['stations']:
        timestamp = station['extra']['last_updated']
        dt_object = timezone.make_aware(datetime.datetime.fromtimestamp(timestamp))
        try:
            extra = Extra.objects.get(uid=station['extra']['uid'])
        except:
            if station['extra']['payment-terminal'] == True:
                extra = Extra(
                    address = station['extra']['address'],
                    altitude = station['extra']['altitude'],
                    ebikes = station['extra']['ebikes'],
                    has_ebikes = station['extra']['has_ebikes'],
                    last_updated = dt_object,
                    normal_bikes = station['extra']['normal_bikes'],
                    payment = station['extra']['payment'],
                    payment_terminal = station['extra']['payment-terminal'],
                    post_code = station['extra']['post_code'],
                    renting = station['extra']['renting'],
                    returning = station['extra']['returning'],
                    slots = station['extra']['slots'],
                    uid = station['extra']['uid'],
                )
                extra.save()
            else:
                extra = Extra(
                    address = station['extra']['address'],
                    altitude = station['extra']['altitude'],
                    ebikes = station['extra']['ebikes'],
                    has_ebikes = station['extra']['has_ebikes'],
                    last_updated = dt_object,
                    normal_bikes = station['extra']['normal_bikes'],
                    payment = station['extra']['payment'],
                    payment_terminal = station['extra']['payment-terminal'],
                    renting = station['extra']['renting'],
                    returning = station['extra']['returning'],
                    slots = station['extra']['slots'],
                    uid = station['extra']['uid'],
                )
                extra.save()
        
        try:
            station = Station.objects.get(id=station['id'])
            list_stations.append(station)
        except:
            station = Station(
                empty_slots = station['empty_slots'],
                extra = extra,
                free_bikes = station['free_bikes'],
                id = station['id'],
                latitude = station['latitude'],
                longitude = station['longitude'],
                name = station['name'],
                timestamp = station['timestamp'],
            )
            station.save()
            list_stations.append(station)
    try:
        response = Response.objects.get(id=data['network']['id'])
    except:
        response = Response(
            company = data['network']['company'],
            gbfs_href = data['network']['gbfs_href'],
            href = data['network']['href'],
            id = data['network']['id'],
            location = location,
            name = data['network']['name'],
            #stations = []
        )
        response.save()
    response.stations.set(list_stations)
    # Obtener los datos de la base de datos y pasarlos al template
    context = {
        'response':response
    }
    return render(request, 'index.html',context)