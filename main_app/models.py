from django.db import models


class WebhookData(models.Model):
    received_data = models.JSONField()
    processed_date = models.DateTimeField(auto_now_add=True)

    order_id = models.CharField(max_length=100, blank=True, null=True)
    customer_name = models.CharField(max_length=200,  blank=True, null=True)
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    order_status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Data received on {self.processed_date}"
