from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import AirPort, AirPlane
from .serializers import AirportsSerializer, AirplanesSerializer


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/airports/',
            'method': 'GET',
            'body': None,
            'desctipion': 'Returns a list of all airports available in the application'
        },
        {
            'Endpoint': '/airports/id',
            'method': 'GET',
            'body': None,
            'desctipion': 'Returns a single airports'
        },
        {
            'Endpoint': '/airplanes/',
            'method': 'GET',
            'body': None,
            'desctipion': 'Returns a list of all airplanes available in the application'
        },
        {
            'Endpoint': '/airplanes/id',
            'method': 'GET',
            'body': None,
            'desctipion': 'Returns a single airplane'
        },
        {
            'Endpoint': '/calculate/',
            'method': 'GET',
            'body': None,
            'desctipion': 'Calculate a time of flight and cost of jet fuel'
        },
    ]
    
    return Response(routes)

@api_view(['GET'])
def getAirports(request):
    airports = AirPort.objects.all()
    serializer = AirportsSerializer(airports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAirport(request, pk):
    airport = AirPort.objects.get(id=pk)
    serializer = AirportsSerializer(airport, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getAirplanes(request):
    airplanes = AirPlane.objects.all()
    serializer = AirplanesSerializer(airplanes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAirplane(request, pk):
    airplane = AirPlane.objects.get(id=pk)
    serializer = AirplanesSerializer(airplane, many=False)
    return Response(serializer.data)