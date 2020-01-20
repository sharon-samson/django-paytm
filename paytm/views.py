from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from . import Checksum
from textiles.models import Order

from paytm.models import PaytmHistory
# Create your views here.

def home(request):
    return HttpResponse("<html><a href='"+ settings.HOST_URL +"/paytm/payment'>PayNow</html>")


def payment(request):
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    get_lang = "/" + get_language() if get_language() else ''
    CALLBACK_URL = settings.HOST_URL + get_lang + settings.PAYTM_CALLBACK_URL
    
    user = request.user
    cust_id = user.username
    checkout_price=0
    incart = Order.objects.filter(ordered_by=user, is_active=True)
    import pdb; pdb.set_trace()
    for order in incart:    
        checkout_price += order.product.price
    
    total = checkout_price
    
    
    
    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()
    # import pdb; pdb.set_trace()
    bill_amount = 100
    if bill_amount:
        data_dict = {
                    'MID':MERCHANT_ID,
                    'ORDER_ID':order_id,
                    'TXN_AMOUNT': total,
                    'CUST_ID':cust_id,
                    'INDUSTRY_TYPE_ID':'Retail',
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL':'http://127.0.0.1:8002/paytm/response/',
                }
        param_dict = data_dict
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request,"paytm/payment.html",{'paytmdict':param_dict, 'orderid': order_id })
    return HttpResponse("Bill Amount Could not find. ?bill_amount=10")


@csrf_exempt
def response(request):
    import pdb; pdb.set_trace()
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            PaytmHistory.objects.create(user=request.user, **data_dict)
            return render(request,"response.html",{"paytm":data_dict})
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)