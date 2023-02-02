from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):

    # product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name")

    # def get_product_count(self, obj):
    #     return Product.objects.filter(category_id == obj.id).count()