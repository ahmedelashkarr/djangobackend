from rest_framework import serializers
from .models import Product 

class productSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_color(self, instance):
        names = []
        for color in instance.color.all():
            names.append(color.color)
        return names


    def get_size(self, instance):
        names = []
        for size in instance.size.all():
            names.append(size.size)
        return names
    def get_brand(self, instance):
        names = []
        for brand in instance.brand.all():
            names.append(brand.brand)
        return names
    



