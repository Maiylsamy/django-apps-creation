from django.http import HttpResponse


def home(request):
    return HttpResponse('-------------------------------use app urls to continue--------------')