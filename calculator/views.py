from django.shortcuts import render


# Create your views here.
def calhome(request):
    return render(request, 'calhome.html')


def caldetials(request):
    num1 = int(request.POST["inpnum1"])
    num2 = int(request.POST["inpnum2"])
    operation = request.POST["oprtn"]

    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "multi":
        result = num1 * num2
    else:
        result = " invalid input"
    return render(request, "calhome.html", {"result": result})
