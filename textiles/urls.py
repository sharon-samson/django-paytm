from django.urls import path
from textiles import views
app_name = 'textiles'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('saree/', views.IndexList.as_view(), name='saree'),
    path('saree/<int:pk>/', views.saree_detail.as_view(), name='saree_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('<int:pk>/buy/', views.buy_view, name='buy'),
    path('order/<int:pk>/delete/', views.OrderDelete.as_view(), name='deleteorder'),
    path('payment/', views.payment, name='payment'),
    path('response/', views.response, name='response'),
    
    
    # path('', views.home, name='home-paytm'),
    # path('payment/', views.payment, name='payment'),
    # path('response/', views.response, name='response'),
]