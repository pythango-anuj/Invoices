from django.shortcuts import HttpResponse
from .serializers import InvoiceSerializer
from .models import Invoice
from rest_framework import generics, status
from rest_framework.response import Response


# /apis
def index(request):
    return HttpResponse("Welcome to invoice app !")


# /apis/invoices/
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


#/apis/invoices/id/
class InvoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
