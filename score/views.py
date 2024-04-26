from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "score.html")


def score(request):
    name = request.POST["name"]
    python = int(request.POST["py"])
    java = int(request.POST["java"])
    mysql = int(request.POST["mysql"])
    html = int(request.POST["html"])
    django = int(request.POST["django"])
    action = request.POST["action"]
    if action == "total":
        p = python + java + mysql + html + django
        if p<=500:
            result = f"{name} your total is {p}"
        else:
            result = "Enter a valid details"
    elif action == "percentage":
        p = (python + java + mysql + html + django) / 500 * 100
        if p<=100:
            result = f"{name} your percentage is {p}"
        else:
            result = "Enter a valid details"
    elif action == "grade":
        p = (python + java + mysql + html + django) / 500 * 100
        if 100 >= p > 90:
            result = "A(Excellent)"
        elif 80 < p < 90:
            result = 'B(Very good)'
        elif 70 < p < 80:
            result = 'C(Good)'
        elif 60 < p < 70:
            result = 'D(Average)'
        elif 50 < p < 60:
            result = 'E(Poor)'
        elif p>100:
            result = "Enter a valid details"
        else:
            result = 'F(Fail)'

    elif action == 'status':
        p = (python + java + mysql + html + django) / 500 * 100
        if p>100:
            result = "Enter a valid details"
        elif p > 50  :
            result = 'PASS(Excellent)'
        else:
            result = 'FAIL'
    data = {"name": name, "python": python, "java": java, "mysql": mysql,
            "html": html, "django": django,"result": result}
    return render(request, "score.html"
                  , data)
