from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from products.models import OrderItem
from products.serializers import *

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.db import transaction
from django.db.models import F

from products.filters import ProductListFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter



is_in_home = openapi.Parameter(
    'home',
    openapi.IN_QUERY,
    description="This query parameter is used to filter data that is shown in the home page.",
    type=openapi.TYPE_BOOLEAN,
)

cid = openapi.Parameter(
    'cid',
    openapi.IN_QUERY,
    description="This query parameter is used to filter data that is shown in the home page.",
    type=openapi.TYPE_STRING,
)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.only('id', 'title', 'short_desc', 'price').order_by('-created_at')
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]

    @swagger_auto_schema(manual_parameters=[is_in_home])
    def get(self, request, *args, **kwargs):
        query_param = request.GET.get('home', None)

        if query_param is not None and query_param == 'true':
            self.queryset = self.queryset[:12]

        return super().get(request, *args, **kwargs)


class ProductFilterListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterser_class = ProductListFilter
    ordering_fields = ['price']


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ManufacturerListAPIView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerListSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CreateOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                items = self.request.data.pop('products')
                order = Order.objects.create(**self.request.data)
                total_price = 0
                for item in items:
                    try:
                        new_order_item = OrderItem.objects.create(order=order, **item)
                        total_price += new_order_item.total_price
                    except OrderItem.DoesNotExist:
                        return Response(data={'error': 'Cart item does not exist.'}, status=400)

                Order.objects.filter(id=order.id).update(total_price=F('total_price') + total_price)
                return Response(data={'order_id': order.id}, status=201)
        except Exception as e:
            return Response(data={'error': str(e)}, status=500)