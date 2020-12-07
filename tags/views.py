from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import status
# from django.http import Http404
from tags.models import Tag
from tags.serializers import TagSerializer
from rest_framework import generics
from rest_framework import viewsets, renderers
from rest_framework import permissions
from rest_framework.decorators import action


#ViewSets

class TagsViewSets(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer