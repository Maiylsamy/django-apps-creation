from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def display_detials(request):
    name = request.POST["txtname"]
    age = request.POST["txtage"]
    course = request.POST["txtcourse"]
    blood = request.POST["blood group"]
    lang = request.POST.getlist('lang',[])
    return render(request,'display.html',
                  {'name': name, 'age': age, 'course': course,
                   'blood': blood, 'lang': lang})
