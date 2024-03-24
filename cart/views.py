from django.shortcuts import render

# Create your views here.
def cart(requests):
    return render(requests,'cart.html')