from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [

    path('home/',views.allPlace,name='allPlace'),
    path('<slug:d_slug>/',views.allPlace,name='place_by_district'),
    # path('<slug:d_slug>/<slug:p_slug>/',views.placeDetail,name='placeDisDetail')
    path('place/<int:place_id>/',views.detail,name='detail'),
    path('place/<int:id>',views.userComments,name='comments'),
    # path('comment/<slug:slug>/', views.post_detail, name='post_detail')
    # path('comment/<int:place_id>/',views.post_detailview,name='post_detail')
    path('image/<int:place_id>/',views.imgReviewdetail,name='imgshow'),
    path('image/<int:id>',views.imgReview,name='imgshows'),
]