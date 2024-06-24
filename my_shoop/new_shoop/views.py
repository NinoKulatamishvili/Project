from django.shortcuts import render
from django.http import HttpResponse
from . models import Clothes
# Create your views here.
def home(request):
    clothes=Clothes.objects.all()
    context = {"clothes": clothes}  #პითონიდან გადავცეთ ინფორმაცია გვერდს
    return render(request, "new_shoop/home.html", context)

def about(request):
    return render(request, "new_shoop/about.html")
