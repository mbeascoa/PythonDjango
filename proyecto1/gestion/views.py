from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Página de inicio </h1> <br/> Hola Benito")