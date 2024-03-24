from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from  .models import Registrations
import random


# Create your views here.
@csrf_exempt
def event(request):
    if request.method == 'POST':
        random_id = random.randint(100000, 999999) 
        name=request.POST.get('name', None)
        phone=request.POST.get('phone', None)
        
        instance = Registrations(id=random_id,name=name,phone=phone)
        instance.save()

    return render(request,'events.html')







