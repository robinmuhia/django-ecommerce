from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import  AllowAny
from item.models import Category, Item
from .serializers import ItemSerializer, CategorySerializer

@api_view(['GET'])
@authentication_classes([])  
@permission_classes([AllowAny])  
def getRoutes(request):
    routes = [
        "GET /api/v1",
        "GET /api/v1/items",
        "GET /api/v1/items/:id",
        "GET /api/v1/category",
    ]
    return Response(routes)

@api_view(['GET'])
@authentication_classes([])  
@permission_classes([AllowAny])  
def getItems(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])  
@permission_classes([AllowAny])  
def getItem(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])  
@permission_classes([AllowAny])  
def getCategory(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
