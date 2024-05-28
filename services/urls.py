from django.urls import path

from services.views import *

urlpatterns = [
    path('', ServiceListAPIView.as_view(), name='services'),
    path('home-services/', ServiceHomeListAPIView.as_view(), name='home-services'),
    path('categories/', ServiceCategoryAPIView.as_view(), name='service-categories'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('order-service/', OrderServiceAPIView.as_view(), name='order-service')
]


