from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.home , name="home"),
    path('signup/', views.signUp , name="signUp"),
    path('login/', views.logIn , name="logIn"),
    path('logOut/',views.logOut , name='logOut'),
    path('adds/', views.Adds , name="Adds"),
    path('edite/', views.EditeUserInfo , name="EditeUserInfo"),
    path('creates/', views.CreateProfile , name="CreateProfile"),
    path('profile/', views.profile , name="profile"),

]
