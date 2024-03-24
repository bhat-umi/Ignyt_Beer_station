from django.shortcuts import render

# Create your views here.
def menu(requests):
    return render(requests,'menu.html')