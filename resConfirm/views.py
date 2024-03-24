from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Reservations

import random

# Create your views here.
@csrf_exempt
def resConfirm(request):
    #return "hello"
    if request.method == 'POST':
        name=request.POST.get('name', '')
        date=request.POST.get('date', '')
        date=date.split('T')[0]
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        description=request.POST.get('desc', '')
        id = random.randint(100000, 999999) 
        instance=Reservations(name=name,date=date,id=id,phone=phone,description=description,email=email)
        instance.save()

   
    return render(request,'resconfirm.html',{'name': name,'date':date,'phone':phone})




