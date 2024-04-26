from django.urls import path

from score import views

urlpatterns = [
    path("",views.home),
    path("read",views.score),
]