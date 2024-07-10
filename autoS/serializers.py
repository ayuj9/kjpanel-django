from .models import ProductImage
from rest_framework import serializers



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields =['id' , 'file']