from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=150,unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def get_url(self):
        return reverse('travel:place_by_district',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Place(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.CharField(max_length=150)
    open = models.BooleanField(default=True)
    image1 = models.ImageField(upload_to='gallery', blank=True)
    image2 = models.ImageField(upload_to='gallery',blank=True)
    image3 = models.ImageField(upload_to='gallery',blank=True)
    image4 = models.ImageField(upload_to='gallery',blank=True)
    location = models.TextField(blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'place'
        verbose_name_plural = 'places'

    def get_url(self):
        return reverse('travel:placeDisDetail',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Comments(models.Model):
    ctext = models.TextField(blank=True)
    cuser = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    cplace = models.ForeignKey(Place,on_delete=models.CASCADE,blank=True,null=True)
    cdate = models.DateField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.cplace)


class ImageReview(models.Model):
    cimage = models.ImageField(upload_to='cimage',blank=True,null=True)
    cuser = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    cplace = models.ForeignKey(Place,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return '{}'.format(self.cplace)
