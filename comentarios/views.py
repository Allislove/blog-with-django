from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import status
# from django.http import Http404
from comentarios.models import Comentario
from comentarios.serializer import ComentarioSerializer
from rest_framework import generics
from rest_framework import viewsets, renderers
from rest_framework import permissions
from rest_framework.decorators import action

#ViewSets

class ComentarioViewSets(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer