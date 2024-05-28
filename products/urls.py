from django.urls import path

from products.views import *

urlpatterns = [
    path('home', ProductListAPIView.as_view(), name='product-list'),
    path('<int:pk>', ProductDetailAPIView.as_view(), name='product-detail'),
    path('manufacturers/', ManufacturerListAPIView.as_view(), name='manufacturers'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('orders/', CreateOrderAPIView.as_view(), name='create-order'),
    path('', ProductFilterListAPIView.as_view(), name='products'),
]

