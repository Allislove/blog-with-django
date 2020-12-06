from django.urls import path, include
from publicaciones import views


urlpatterns = [
    path('publicaciones/', views.PublicationList),
    path('publicaciones/<int:id>/', views.Publication_detail),


]