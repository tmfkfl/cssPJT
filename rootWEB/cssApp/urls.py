from django.urls import path
from cssApp import views

urlpatterns = [

    path("main/", views.index),
    path("external/", views.external),
    path("selector/", views.selector),
    path("descendant/", views.descendant),
    path("box/", views.box),
    path("layout/", views.layout),
]