from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from pokemon_gen3 import Nature, Pokemon


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if "pokemon_button" in request.POST:
            ...
    context = {
        "pokemons": [p.name_jp for p in Pokemon],
        "natures": [n.name_jp for n in Nature],
    }
    return render(request, "index.html", context)
