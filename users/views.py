from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import VendorSerializer, CustomerSerializer, MyTokenObtainPairSerializer
from .models import Vendor, Customer
from rest_framework import permissions, status
from .permissions import AnonPermission


class LoginView(TokenObtainPairView):
    permission_classes = (AnonPermission,)
    serializer_class = MyTokenObtainPairSerializer


class VendorRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    # parser_classes = JSONParser

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            vendor = Vendor.objects.create(
                email=request.data['email'],
                is_Vendor=True,
                name=request.data['name'],
                second_name=request.data['second_name'],
                phone_number=request.data['phone_number'],
                description=request.data['description']
            )
            vendor.set_password(request.data['password'])
            vendor.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    # authentication_classes = []
    # parser_classes = JSONParser

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = Customer.objects.create(
                email=request.data['email'],
                name=request.data['name'],
                second_name=request.data['second_name'],
                phone_number=request.data['phone_number'],
                cart_number=request.data['cart_number'],
                address=request.data['address'],
                post_code=request.data['post_code'],
            )
            customer.set_password(request.data['password'])
            customer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request):
        snippets = Vendor.objects.all()
        serializer = VendorSerializer(snippets, many=True)
        return Response(serializer.data)


class CustomerListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    # authentication_classes = []

    def get(self, request):
        snippets = Customer.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)


class VendorDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get_object(self, id):
        try:
            return Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            raise Http404

    def get(self, request, id):
        snippet = self.get_object(id)
        serializer = VendorSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id):
        snippet = self.get_object(id)
        serializer = VendorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    # authentication_classes = []

    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, id):
        snippet = self.get_object(id)
        serializer = CustomerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id):
        snippet = self.get_object(id)
        serializer = CustomerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






