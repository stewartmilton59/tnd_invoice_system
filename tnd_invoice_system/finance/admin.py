from django.contrib import admin
from .models import District, FacilityRecord

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name", "tin_number")

@admin.register(FacilityRecord)
class FacilityRecordAdmin(admin.ModelAdmin):
    list_display = ("facility_name", "district", "invoice_number", "invoice_amount", "amount_paid", "balance")
    list_filter = ("district", "invoice_date")
    search_fields = ("facility_name", "invoice_number")