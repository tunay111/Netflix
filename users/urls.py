from django.urls import path
from .views import *
urlpatterns=[
    path("register",register,name="register"),
    path("login",userLogin,name="login"),
    path("browse",profiles,name="profiles"),
    path("create-profile",createProfil,name="create-profile"),
    path("logout",oturumKapat,name="logout"),
    path("hesap",userProfil,name="hesap"),
    path("delete",deleteUser,name="delete"),
]