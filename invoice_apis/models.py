from django.db import models
from datetime import datetime

# Invoice model
class Invoice(models.Model):
    customer_name = models.CharField(max_length=50, verbose_name = "Customer Name")
    date = models.DateField(default=datetime.now, verbose_name = "Date")
    
    def __str__(self) -> str:
        return self.customer_name + " " + str(self.date)


# Invoice details model
class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete = models.CASCADE, related_name="invoice_details")
    description = models.TextField(verbose_name = "Invoice Description")
    quantity = models.IntegerField(verbose_name = "Qunatity(No of Units)")
    unit_price = models.IntegerField(verbose_name = "Unit Price")
    price = models.BigIntegerField(verbose_name = "Total Price")
    
