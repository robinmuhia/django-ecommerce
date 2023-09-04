from rest_framework import serializers
from item.models import Category,Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )
        
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'category',
            'id',
            'name',
            'description',
            'is_sold',
            'created_by',
        )