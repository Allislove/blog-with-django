from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import status
# from django.http import Http404
from publicaciones.models import Publicacion
from publicaciones.serializers import PublicationSerializer
from comentarios.serializer import ComentarioSerializer
from comentarios.models import Comentario
from tags.serializers import TagSerializer
from rest_framework import viewsets

# from rest_framework import generics
# from rest_framework import permissions
from rest_framework.decorators import action




#Vistas genericas
# class PublicationList(generics.ListCreateAPIView):
#     queryset = Publicacion.objects.all()
#     serializer_class = PublicationSerializer
#
# class Publication_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Publicacion.objects.all()
#     serializer_class = PublicationSerializer



#ViewSets

class PublicationViewSets(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicationSerializer

    @action(methods=['GET'], detail=True)
    #Voy a buscar los comentarios que existan en la publicacion #id
    def comentarios(self, request, pk=None):
        #Guardamos la publicacion
        publicacion = self.get_object()
        if request.method == 'GET':
            #Busco la referencia a la cual quiero hacer la consulta,
            #Ejemplo busco la referencia del contenido de la publicacion en cuestion del numero de la publicacion
            serializer = ComentarioSerializer(publicacion.comentario, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)


    @action(methods=['DELETE'], detail=True)
    def comentario(self, request, pk=None):
        comentario = self.get_object()
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            comentario.delete()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['POST'], detail=True)
    def post_comment(self, request, pk=None):
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #Si la peticion es satisfactoria manda un status 201
            return Response(status=status.HTTP_201_CREATED)
            #De lo contrario muestra unstatus 400 de error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['GET'], detail=True)
    # Voy a buscar los comentarios que existan en la publicacion #id
    def tag(self, request, pk=None):
        publicacion = self.get_object()
        if request.method == 'GET':
            serializer = TagSerializer(publicacion.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)






# Create your views here.
#Escribiendo vistas basadas en funciones restTutoria

#Vistas basadas en clase
# class PublicationList(APIView):
#     #Defino los metodos
#     def get(self, request, format=None):
#         publicacion = Publicacion.objects.all()
#         serializer = PublicationSerializer(publicacion, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#
#         serializer = PublicationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#
# class Publication_detail(APIView):
#     #Voy a pedir que me regrese el id
#     def get_object(self, id):
#         try:
#             return Publicacion.objects.get(id=id)
#         except Publicacion.DoesNotExist:
#             raise Http404
#
#     def get(self, request, id, format=None):
#         publicacion = self.get_object(id)
#         serializer = PublicationSerializer(publicacion)
#         #Ahora cogemos el objeto de la respuesta serializada
#         return Response(serializer.data)
#
#     def put(self, request, id, format=None):
#         publicacion = self.get_object(id)
#         serializer = PublicationSerializer(publicacion, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id, format=None):
#         publicacion = self.get_object(id)
#         publicacion.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#Vistas genericas




#Vistas basadas en funciones
# @api_view(['GET', 'POST'])
# def PublicationList(request):
#     if request.method == 'GET':
#         publicacion = Publicacion.objects.all()
#         serializer = PublicationSerializer(publicacion, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#     elif request.method == 'POST':
#         serializer = PublicationSerializer(data=request.data)
#         if serializer.is_Valid():
#             serializer.save()
#             #Si la peticion es satisfactoria manda un status 201
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         #De lo contrario muestra unstatus 400 de error
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def Publication_detail(request, id):
#     #Para mostrar una publicacion en especifica y asi eliminarla o editarla
#     try:
#         #Vamos a buscar la publicacion si existe muestrame de lo contrario muestranos un error
#         publicacion = Publicacion.objects.get(id=id)
#     except Publicacion.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PublicationSerializer(publicacion)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = PublicationSerializer(publicacion, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         publicacion.delete()
#         return Response(status=status.HTTP_200_OK)
#     else:
#         return Response({'No se ha podido eliminar la publicacion :/ '},' ', status=status.HTTP_400_BAD_REQUEST)
