from django.urls import path
from paytm import views
app_name = 'paytm'

urlpatterns = [
    # path('home/', views.Home.as_view(), name='home'),
    path('', views.home, name='home-paytm'),
    path('payment/', views.payment, name='payment'),
    path('response/', views.response, name='response'),
]