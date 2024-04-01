from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductModel
from .serializers import ProductSerializers
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
@api_view(['GET'])
def product(request):
    product = ProductModel.objects.all()
    product_serializers = ProductSerializers(product, many = True, context = {'request': request})
    return Response(product_serializers.data)

