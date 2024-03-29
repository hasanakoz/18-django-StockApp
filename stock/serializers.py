from rest_framework import serializers
from .models import Category, Product,Brand, Firm, Purchase, Sales
import datetime
class CategorySerializer(serializers.ModelSerializer):

    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "product_count")

    def get_product_count(self, obj):
        return Product.objects.filter(category_id = obj.id).count()



class ProductSerializer(serializers.ModelSerializer):

    brand_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = (
        "id",
        "name",
        "category",
        "category_id",
        "brand", 
        "brand_id",
        "stock",
    )
    read_only_fields = ('stock',)



class CategoryProductSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "product_count", "products")

    def get_product_count(self, obj):
        return Product.objects.filter(category_id = obj.id).count()

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "image"
        )


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            "id",
            "name",
            "phone",
            "image",
            "address"
        )


class PurchaseSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    firm = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    category = serializers.SerializerMethodField()
    time_hour = serializers.SerializerMethodField()
    createds = serializers.SerializerMethodField()
    class Meta:
        model = Purchase
        fields = (
            "id",
            "user",
            "user_id",
            "category",
            "firm",
            "firm_id",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",
            "createds",
            "time_hour",
        )
    def get_category(self, obj):
        product = Product.objects.get(id=obj.product_id)
        return Category.objects.get(id=product.category_id).name

    def get_createds(self, obj):
        return datetime.datetime.strftime(obj.createds, "%d:%m:%Y")

    def get_time_hour(self, obj):
        return datetime.datetime.strftime(obj.createds, "%H:%M")


class SalesSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    # category = serializers.SerializerMethodField()
    time_hour = serializers.SerializerMethodField()
    createds = serializers.SerializerMethodField()
    class Meta:
        model = Sales
        fields = (
            "id",
            "user",
            "user_id",
            # "category",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",            
            "time_hour",
            "createds",
        )
    # def get_category(self, obj):
    #     product = Product.objects.get(id=obj.product_id)
    #     return Category.objects.get(id=product.category_id).name

    def get_createds(self, obj):
        return datetime.datetime.strftime(obj.createds, "%d:%m:%Y")

    def get_time_hour(self, obj):
        return datetime.datetime.strftime(obj.createds, "%H:%M")