from django.urls import path

from calculator import views

urlpatterns=[
    path("",views.calhome),
    path("read",views.caldetials)
]