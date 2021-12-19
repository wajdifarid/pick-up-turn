from collections import defaultdict
from collector_app.models.collection import Collection
from collector_app.forms import CollectionForm
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views import View
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.db import transaction
from django.contrib import messages


@transaction.atomic
def collect(request, *args, **kwargs):
    form = CollectionForm()
    collection_data, current_person = get_turn_data()
    return render(
        request,
        "index.html",
        {
            "form": form,
            "collection_data": collection_data,
            "current_turn": current_person,
        },
    )


def get_collection(request, *args, **kwargs):
    if request.method == "POST":
        form = CollectionForm(request.POST)

        if form.is_valid():
            messages.success(request, "Data pengambilan telah disimpan")
            collection = form.save(commit=False)
            collection.collector = request.user
            collection.save()
            form = CollectionForm()
            collection_data, current_person = get_turn_data()
            return render(
                request,
                "index.html",
                {
                    "form": form,
                    "collection_data": collection_data,
                    "current_turn": current_person,
                },
            )
        return HttpResponse("mantab")

    collections = Collection.objects.all()
    return render(request, "collections.html", {"collections": collections})


def get_turn_data():
    collection_data = defaultdict(int)
    users = User.objects.all()

    collection_salman = Collection.objects.filter(
        collector=users.filter(username="salman").first()
    ).count()
    collection_farid = Collection.objects.filter(
        collector=users.filter(username="farid").first()
    ).count()
    collection_faizah = Collection.objects.filter(
        collector=users.filter(username="faizah").first()
    ).count()

    collection_data["salman"] = collection_salman 
    collection_data["farid"] = collection_farid 
    collection_data["faizah"] = collection_faizah 
    

    tmp_data = []
    tmp_data.append((collection_data["salman"], -2, "salman"))
    tmp_data.append((collection_data["farid"], -1, "farid"))
    tmp_data.append((collection_data["faizah"], 0, "faizah"))
    tmp_data.sort()
    return collection_data, tmp_data[0][2]
