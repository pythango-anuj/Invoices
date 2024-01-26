from django.urls import path
from .views import index, InvoiceListCreateView, InvoiceRetrieveUpdateDestroyView

urlpatterns = [
    path('', index, name="index"),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveUpdateDestroyView.as_view(), name='invoice-retrieve-update-destroy'),
]
