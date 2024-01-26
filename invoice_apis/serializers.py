# serializers.py
from rest_framework import serializers
from .models import Invoice, InvoiceDetails

class InvoiceDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = InvoiceDetails
        fields = ['id', 'description', 'quantity', 'unit_price', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = InvoiceDetailsSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'customer_name', 'date', 'invoice_details']

    def create(self, validated_data):
        invoice_details_data = validated_data.pop('invoice_details', [])
        invoice = Invoice.objects.create(**validated_data)

        for detail_data in invoice_details_data:
            InvoiceDetails.objects.create(invoice=invoice, **detail_data)

        return invoice

    def update(self, instance, validated_data):
        invoice_details_data = validated_data.pop('invoice_details', [])

        # Update Invoice instance fields
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        # Get existing InvoiceDetails instances
        existing_details = instance.invoice_details.all()

        # Update or delete existing instances
        for existing_detail in existing_details:
            matching_data = next(
                (detail_data for detail_data in invoice_details_data
                 if self.matching_data(existing_detail, detail_data)),
                None
            )

            if matching_data:
                # If matching data is found, update the existing InvoiceDetails instance
                self.update_invoice_detail(existing_detail, matching_data)
            else:
                # If no matching data is found, delete the existing InvoiceDetails instance
                existing_detail.delete()

        # Create new InvoiceDetails instances for remaining data
        for detail_data in invoice_details_data:
            if not self.matching_data_exists(existing_details, detail_data):
                # If no matching data exists, create a new InvoiceDetails instance
                InvoiceDetails.objects.create(invoice=instance, **detail_data)

        return instance

    def matching_data(self, existing_detail, detail_data):
        # Define your logic for matching data here
        return (
            existing_detail.description == detail_data.get('description') and
            existing_detail.quantity == detail_data.get('quantity') and
            existing_detail.unit_price == detail_data.get('unit_price') and
            existing_detail.price == detail_data.get('price')
        )

    def matching_data_exists(self, existing_details, detail_data):
        # Check if matching data already exists in the list of existing details
        return any(self.matching_data(existing_detail, detail_data) for existing_detail in existing_details)

    def update_invoice_detail(self, existing_detail, detail_data):
        # Use this method to update an existing InvoiceDetails instance
        existing_detail.description = detail_data.get('description', existing_detail.description)
        existing_detail.quantity = detail_data.get('quantity', existing_detail.quantity)
        existing_detail.unit_price = detail_data.get('unit_price', existing_detail.unit_price)
        existing_detail.price = detail_data.get('price', existing_detail.price)
        existing_detail.save()
