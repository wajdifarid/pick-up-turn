from collector_app.views import get_collection
from django.urls import path

urlpatterns = [
     path('', get_collection, name='collections'),
]
