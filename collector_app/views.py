from typing import Collection
from collector_app.forms import CollectionForm
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime 
from django.views import View
from django.forms import modelformset_factory


def collect(request, *args, **kwargs):
    form = CollectionForm()
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.collector = request.user
            collection.save()
            return HttpResponse('mantab')
        return HttpResponse('mantab')
    
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    form = CollectionForm()
    return render(request, 'index.html', {'form': form})
