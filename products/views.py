from django.shortcuts import get_object_or_404
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET' , 'POST'])

def product_list(request):

    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer (products, many = True)
        return Response (serializer.data, status = status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid (raise_exception= True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view (["GET", "PUT", "DELETE"])
def product_detail(request, pk):
    products = get_object_or_404 (Product, pk=pk)   
    if request.method == "GET":  
        serializer = ProductSerializer(products)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ProductSerializer(products, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        products.delete()
        return Response(status.HTTP_204_NO_CONTENT)
