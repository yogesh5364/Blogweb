from django.http import HttpResponse

def index(request):
    return HttpResponse("THIS IS MY DJANGO PROJECT")

def home(request):
    return HttpResponse("<h1 style='color:red'>THIS IS HOME</h1>")


# python manage.py runserver localhost:80