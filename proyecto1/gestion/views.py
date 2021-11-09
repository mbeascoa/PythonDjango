#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("<h1>Página de inicio </h1> <br/> Hola Benito")


from django.shortcuts import render

def index(request):
    return render(request, "gestion/Inicio.html")


def equipo(request):
    nombre='Real Madrid'
    dato=nombre.upper()
    lista={
        "equipo1":dato
    }
    return render(request, "gestion/equipoPreferido.html",lista)



def jugadores(request):
    listajugadores=[
        {
            "Nombre":"Sergio Ramos",
            "Demarcacion":"Defensa",
            "Numero":5
        },
        {
            "Nombre": "Eden Hazard",
            "Demarcacion": "Delantero",
            "Numero":7
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero":8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]
    contexto = {
        'listado_jugadores': listajugadores
    }
    return render(request, "gestion/jugadores.html",contexto)

def amistades(request):
    listaamigos=[
                    { "Nombre": "Ana" },
                    {"Nombre": "AnaLinda"},
                    {"Nombre": "AnaRosa"},
                    {"Nombre": "Begoña"},
                    {"Nombre": "Legorburu"},
                    {"Nombre": "Belausteguigoitia"},
                    {"Nombre": "Berasategui"},
                    {"Nombre": "Bermúdez"},
                    {"Nombre": "Bengoechea"},
                    {"Nombre": "Gabicagogeascoa"},
                    {"Nombre": "Landa"},
                    {"Nombre": "Beitia"},
                    {"Nombre": "Badiola"},
                    {"Nombre": "Bárcenas"},
                    {"Nombre": "Zamudio"},
                    {"Nombre": "Zandibar"}

    ]
    contexto = {
        'listado_amistades': listaamigos
    }
    return render(request, "gestion/amigos.html", contexto)