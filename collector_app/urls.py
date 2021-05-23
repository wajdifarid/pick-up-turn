from collector_app.views import collect
from django.urls import path

urlpatterns = [
     path('', collect),
]
