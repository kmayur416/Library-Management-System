
from ast import Delete
from dataclasses import fields
from rest_framework import serializers
from .models import *

class Bookserializer(serializers.ModelSerializer):
    # id = serializers.CharField()
    # book_name = serializers.CharField(max_length=50,required=False)
    # author_name = serializers.CharField(max_length=50,required=False)
    # category = serializers.CharField(max_length=50, required=False)
    # stock_quantity = serializers.IntegerField(required=False)
    # created = serializers.DateField(required=False)
    # modified = serializers.DateField(required=False)
    # language = serializers.CharField (max_length =10,required=False)

    # def create(self, validated_data):
    #     return Book.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     return Book.objects.update(**validated_data)
    
    class Meta:
        model = Book
        fields = "__all__"