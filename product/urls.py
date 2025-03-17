from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.favourite_list, name='wishlist'),
    path('add_to_wishlist/<int:id>/', views.favourite_add, name='add_to_wishlist'),
    path('search/', views.search, name='search'),
    path('', views.ProductView.as_view(), name='products'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('order_summary/', views.OrderSummary.as_view(), name='order_summary'),
    path('<slug>/', views.productdetail, name='productdetail'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove-single-item-from-cart/<slug>/', views.remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('payment/<payment_option>/', views.PaymentView.as_view(), name='payment'),
    path('request-refund/', views.RequestRefundView.as_view(), name='request-refund'),
    path('add-coupon/', views.AddCouponView.as_view(), name='add-coupon'),
]
