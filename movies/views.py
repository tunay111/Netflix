from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def anaSayfa(request):
    return render(request,"index.html")

def browse_index(request):
    filmler=Movies.objects.all()
    search_movie=""
    if request.GET.get("search_movie"):
        search_movie=request.GET.get("search_movie")
        filmler=filmler.filter(
            Q(filmismi__icontains=search_movie)  |
            Q(kategori__name__icontains=search_movie)  
            # Q(tur__name__icontains=search_movie)
        )
    context={}
    try:
        izleyen=Izlenen.objects.get(user=request.user)
        izlenen=izleyen.izlenen.all()
        context={
            "filmler":filmler,
            "izlenen":izlenen,
            "search_movie":search_movie
        }
    except:
        context={
        "filmler":filmler,
        "search_movie":search_movie
    }
    return render(request,"browse-index.html",context)