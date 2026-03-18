from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tin_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class FacilityRecord(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="facilities")
    facility_name = models.CharField(max_length=200)
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()
    invoice_amount = models.DecimalField(max_digits=20, decimal_places=2)
    payment_date = models.DateField(blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.facility_name} ({self.district.name})"