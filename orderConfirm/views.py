from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import json
from .models import Order
from datetime import datetime
# Create your views here.


from django.views.decorators.csrf import csrf_exempt


import random

# Create your views here.


def generate_order_id():
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

    # Combine prefix "IG-" with the random string
    order_id = f"IG-{random_part}"

    return order_id
@csrf_exempt
def orderConfirm(request):
    print("#######",request.method)
    if request.method!='POST':
        return HttpResponse("")
    total=request.POST.get('total', '')
    cart=request.POST.get('cart', 'empty cart')
    cart=json.loads(cart)
    amount=0;
    for item in  cart['items']:
        amount+=int(item['price'])
    id=generate_order_id()
    instance=Order(id=id,total=amount,items=cart['items'],timestamp=datetime.now())
    instance.save()

    
    return render(request,'orderconfirm.html', {'amount': amount,'orderid':id})