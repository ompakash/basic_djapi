from rest_framework import serializers
from .models import products

class productsSerializers(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ("id","name", "description", "price", )