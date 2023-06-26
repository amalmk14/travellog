from django.contrib import admin
from .models import *

# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(District,DistrictAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Place,PlaceAdmin)

admin.site.register(Comments)
admin.site.register(ImageReview)