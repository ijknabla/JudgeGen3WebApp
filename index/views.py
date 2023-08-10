from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if "pokemon_button" in request.POST:
            ...
    return render(request, "index.html")
