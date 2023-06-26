from django.shortcuts import render
from travel.models import Place
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def searchResult(request):
    places = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        places = Place.objects.all().filter(Q(name__contains=query) | Q(description__contains=query) | Q(city__contains=query))
    return render(request,'search.html',{'query':query,'places':places})

