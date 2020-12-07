from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from publicaciones import views
from rest_framework.routers import DefaultRouter



# from django.urls import path, include

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api/v1/publicaciones', views.PublicationViewSets)

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls

# urlpatterns = [
#     # path('', views.api_root),
#     # path('publicacioniones/<int:pk>/publicacion/', views.PublicationViewSets.as_view()),
#     path('publicaciones/', views.PublicationList.as_view()),
#     path('publicaciones/<int:pk>/', views.Publication_detail.as_view()),
#     path('viewset', views.PublicationViewSets.as_view())
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)