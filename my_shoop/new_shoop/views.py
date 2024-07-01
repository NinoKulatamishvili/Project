from django.shortcuts import render
from django.http import HttpResponse
from . models import Products, User
from . models import Categories

# Create your views here.
def home(request):
    products=Products.objects.all()
    context = {"products": products}  #პითონიდან გადავცეთ ინფორმაცია გვერდს
    return render(request, "new_shoop/home.html", {'products': products})

def about(request):
    return render(request, "new_shoop/about.html")

def profile(request, ms):
    user=User.objects.get(id=ms)
    products=user.products.all()
    context = {"products": products}
    return render(request, "new_shoop/profile.html", context)
