# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from publicaciones.models import Publicacion
from publicaciones.serializers import PublicationSerializer

# Create your views here.
#Escribiendo vistas basadas en funciones restTutorial

@api_view(['GET', 'POST'])
def PublicationList(request):
    if request.method == 'GET':
        publicacion = Publicacion.objects.all()
        serializer = PublicationSerializer(publicacion, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_Valid():
            serializer.save()
            #Si la peticion es satisfactoria manda un status 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #De lo contrario muestra unstatus 400 de error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Publication_detail(request, id):
    #Para mostrar una publicacion en especifica y asi eliminarla o editarla
    try:
        #Vamos a buscar la publicacion si existe muestrame de lo contrario muestranos un error
        publicacion = Publicacion.objects.get(id=id)
    except Publicacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PublicationSerializer(publicacion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PublicationSerializer(publicacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        publicacion.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({'No se ha podido eliminar la publicacion :/ '},' ', status=status.HTTP_400_BAD_REQUEST)
