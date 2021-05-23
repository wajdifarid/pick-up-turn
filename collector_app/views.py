from collections import defaultdict
from collector_app.models import CollectionCount
from typing import Collection
from collector_app.forms import CollectionForm
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime 
from django.views import View
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.db import transaction

@transaction.atomic
def collect(request, *args, **kwargs):
    form = CollectionForm()
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.collector = request.user
            collection.save()
            collection_count = CollectionCount.objects.filter(collector=request.user).first()
            if collection_count is None:
                collection_count = CollectionCount(collector=request.user, collect_count=0)
                collection_count.save()
            collection_count.collect_count += 1
            collection_count.save()
            return HttpResponse('mantab')
        return HttpResponse('mantab')
    
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    form = CollectionForm()
    collection_data = defaultdict(int)
    users = User.objects.all()
    
    collection_salman = CollectionCount.objects.filter(collector=users.filter(username="salman").first()).first()
    collection_farid = CollectionCount.objects.filter(collector=users.filter(username="farid").first()).first()
    collection_faizah = CollectionCount.objects.filter(collector=users.filter(username="faizah").first()).first()

    collection_data['salman'] = collection_salman.collect_count if collection_salman is not None else 0
    collection_data['farid'] = collection_farid.collect_count if collection_farid is not None else 0
    collection_data['faizah'] = collection_faizah.collect_count if collection_faizah is not None else 0

    return render(request, 'index.html', {'form': form, 'collection_data':collection_data})
