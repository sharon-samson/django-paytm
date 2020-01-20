from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from textiles.models import Product, ProductImage, Order
from django.views.generic.base import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from textiles import Checksum
from textiles.models import Order, PaytmHistory


# Create your views here.

# def home(request):
#     return render(request, 'textiles/home.html', {})

class Home(TemplateView):
    template_name = 'textiles/home.html'

class IndexList(View):
    template_name = 'textiles/saree.html'
    queryset = Product.objects.filter(product_type="Saree")

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        image = ProductImage.objects.get(product=self.queryset[0])
        context = { 'object_list': self.get_queryset, 'image': image   }
        return render(request, self.template_name, context)

class saree_detail(View):
    template_name = 'textiles/saree_detail.html'

    def get_object(self):
        id = self.kwargs.get('pk')
        obj= None
        if id is not None:
            obj = get_object_or_404(Product, id=id)
        return obj
    
    def get(self, request, *args, **kwargs):
        image = ProductImage.objects.get(product=self.get_object())
        context = { 'saree': self.get_object(), 'image': image }
        # ordered_by = request.user
        # order_id = paytm.Checksum.__id_generator__()
        # product = self.get_object()
        # Order.objects.create(ordered_by=ordered_by, order_id=order_id, product=product)
        return render(request, self.template_name, context)

    
def buy_view(request, pk, **kwargs):
    context = {}
    # id = request.kwargs.get('pk')
    obj= None
    if id is not None:
        obj = get_object_or_404(Product, id=pk)
    ordered_by = request.user
    # order_id = Checksum.__id_generator__()
    product = obj
    Order.objects.create(ordered_by=ordered_by, product=product)
    return redirect('textiles:cart')
        
        
def cart_view(request, *args, **kwargs):
    user = request.user 
    checkout_price=0
    # image = ProductImage.objects.get(product=self.get_object())
    incart = Order.objects.filter(ordered_by=user, is_active=True)
    # request.session['user'] = user
    for order in incart:    
        checkout_price += order.product.price
        try:
            image = ProductImage.objects.get(product=order.product)
        except:
            pass
    
    total = checkout_price
    try:
        images = image
    except:
        pass
    return render(request, 'textiles/cart.html', {'cart': incart, 'total': total, 'image': images})


class OrderDelete(View):
    template_name = 'textiles/order_confirm_delete.html'

    def get_object(self):
        id = self.kwargs.get('pk')
        obj= None
        if id is not None:
            obj = get_object_or_404(Order, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('textiles:cart')
        return render(request, self.template_name, context) 

def payment(request):
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    get_lang = "/" + get_language() if get_language() else ''
    CALLBACK_URL = settings.HOST_URL + get_lang + settings.PAYTM_CALLBACK_URL
    # import pdb; pdb.set_trace()
    user = request.user
    cust_id = user.username
    checkout_price=0
    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()
    incart = Order.objects.filter(ordered_by=user, is_active=True)
    for order in incart:    
        checkout_price += order.product.price
        order.order_id = order_id
        order.save()
    total = checkout_price
    
    
    
    
    # import pdb; pdb.set_trace()
    bill_amount = 100
    if bill_amount:
        data_dict = {
                    'MID':MERCHANT_ID,
                    'ORDER_ID':order_id,
                    'TXN_AMOUNT': bill_amount,
                    'CUST_ID':cust_id,
                    'INDUSTRY_TYPE_ID':'Retail',
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL':'http://colourplus.live/response/',
                }
        param_dict = data_dict
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request,"paytm/payment.html",{'paytmdict':param_dict, 'orderid': order_id })
    return HttpResponse("Bill Amount Could not find. ?bill_amount=10")


@csrf_exempt
def response(request):
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            PaytmHistory.objects.create(**data_dict)
            incart = Order.objects.filter(order_id=data_dict['ORDERID'], is_active=True)
            for order in incart:
                order.is_active = False
                order.save()
            return render(request,"paytm/response.html",{"paytm":data_dict})

        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)