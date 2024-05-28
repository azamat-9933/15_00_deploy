from rest_framework import serializers

from products.models import (
    ProductImage, Product, Instruction, Order, Manufacturer, Category
)
from common.serializers import MediaURLSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = ProductImage
        exclude = ["product"]
        read_only_fields = ["id", "image"]


class CharacteristicValueSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    values = CharacteristicValueSerializer(many=True)


class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    short_desc = serializers.CharField()
    price = serializers.FloatField()
    product_images = ProductImageSerializer()


class InstructionSerializer(serializers.ModelSerializer):
    right_image = MediaURLSerializer()
    left_image = MediaURLSerializer()

    class Meta:
        model = Instruction
        exclude = ['product']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    product_images = ProductImageSerializer(many=True)
    characteristics = CharacteristicSerializer(many=True)
    instructions = InstructionSerializer(many=True)
    recommended_products = serializers.SerializerMethodField()  # method

    class Meta:
        model = Product
        exclude = ['view_count', 'manufacturer', 'created_at']
        read_only_fields = ['id', 'title', 'description', 'discount',
                            'price', 'product_images', 'category',
                            'short_desc', 'recommended_products']

    def get_recommended_products(self, obj):
        recommended_products = Product.objects.filter(category_id=obj.category_id).exclude(id=obj.id)[:8]
        return ProductListSerializer(recommended_products, many=True).data


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.ModelSerializer):
    products = serializers.ListSerializer(child=OrderItemSerializer())

    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'products')


class ManufacturerListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, obj):
        return obj.product_set.count()


class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'products_count')

    def get_products_count(self, obj):
        return obj.product_set.count()
