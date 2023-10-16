from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import productSerializer
from .models import Product
from rest_framework import generics
# Create your views here.


class api(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer


@api_view()
def api_details(req, slug):
    pro_details = Product.objects.get(slug=slug)
    data = productSerializer(pro_details).data
    return Response(data)
