from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def allPlace(request,d_slug=None):
    d_page = None
    places = None
    if d_slug != None:
        d_page = get_object_or_404(District,slug=d_slug)
        places = Place.objects.all().filter(district=d_page)
    else:
        places = Place.objects.all().filter()
    paginator = Paginator(places,16)
    try:
        page = int(request.GET.get('page',"1"))
    except:
        page = 1
    try:
        places = paginator.page(page)
    except (EmptyPage, InvalidPage):
        places = paginator.page(paginator.num_pages)
    return render(request,'districts.html',{'district':d_page,'places':places})

# def placeDetail(request,d_slug,p_slug):
#     try:
#         place = Place.objects.get(district__slug=d_slug,slug=p_slug)
#     except Exception as e:
#         raise e
#     return render(request,'place.html',{'place':place})

@login_required(login_url='/login/')
def detail(request,place_id):
    place = Place.objects.get(id=place_id)
    com = Comments.objects.filter(cplace_id=place_id)
    user = request.user
    return render(request,'place.html',{'place':place,'user': user, 'comments': com})

@login_required(login_url='/login/')
def userComments(request,id):
    com = Comments.objects.filter(cplace_id=id)
    user = request.user
    if request.method == 'POST':
        place = Place.objects.get(id=id)
        user = request.user
        ctext = request.POST['ctext']
        # cimage = request.FILES['cimage']
        comments = Comments(ctext=ctext,cplace=place,cuser=user)
        comments.save()
        return render(request, 'place.html',{'place':place,'user': user, 'comments': com})
    return render(request, 'place.html', { 'user': user, 'com': com})

@login_required(login_url='/login/')
def imgReview(request,id):
    com = ImageReview.objects.filter(cplace_id=id)
    user = request.user
    if request.method == 'POST':
        place = Place.objects.get(id=id)
        user = request.user
        # ctext = request.POST['ctext']
        cimage = request.FILES['cimage']
        comments = ImageReview(cimage=cimage,cplace=place,cuser=user)
        comments.save()
        return render(request, 'image.html',{'place':place,'user': user, 'comments': com})
    return render(request, 'image.html', { 'user': user, 'com': com})

@login_required(login_url='/login/')
def imgReviewdetail(request,place_id):
    place = Place.objects.get(id=place_id)
    com = ImageReview.objects.filter(cplace_id=place_id)
    user = request.user
    return render(request,'image.html',{'user': user, 'comments':com,'place':place})