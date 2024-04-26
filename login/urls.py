from django.urls import path

from login import views

urlpatterns = [
    path('',views.home),
    path('display',views.display_detials),

]