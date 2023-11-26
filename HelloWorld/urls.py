from django.urls import path
from HelloWorld import views

urlpatterns = [
    path("",views.home, name="home"),
]