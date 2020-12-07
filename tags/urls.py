from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tags import views
from rest_framework.routers import DefaultRouter



# from django.urls import path, include

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api/v1/tags', views.TagsViewSets)

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls