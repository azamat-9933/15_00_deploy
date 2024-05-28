from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from services.serializers import *


class ServiceHomeListAPIView(ListAPIView):
    queryset = Service.objects.filter(is_home_page=True)
    serializer_class = ServiceHomeListSerializer


class ServiceCategoryAPIView(ListAPIView):
    queryset = ServiceCategory.objects.filter(parent__isnull=True)
    serializer_class = ServiceCategoryListSerializer


class ServiceListAPIView(ListAPIView):  # чтения больше чем 1 экземпляра
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer

    # SORT by category


class ServiceDetailView(RetrieveAPIView):  # чтения 1 экземпляра
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer


class OrderServiceAPIView(CreateAPIView):
    queryset = OrderService.objects.all()
    serializer_class = OrderServiceSerializer
