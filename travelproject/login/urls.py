from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'login'

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path("register/", views.SignUp, name="signup"),
    path('profile/<int:pk>/',views.userProfile,name='profile'),
    path("editprofile/<int:pk>/", views.updateUser, name="editprofile"),

]