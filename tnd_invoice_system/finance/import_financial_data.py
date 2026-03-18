import pandas as pd
from datetime import datetime
from finance.models import District, FacilityRecord

def run():
    # Load the Excel file
    df = pd.ExcelFile("MWANZA SECRETARIATE FINANCIAL STATEMENT.xlsx")

    # Loop through each sheet (district)
    for sheet_name in df.sheet_names:
        print(f"Processing sheet: {sheet_name}")
        data = df.parse(sheet_name)

        # Create or get District
        district, _ = District.objects.get_or_create(
            name=sheet_name.strip(),
            defaults={"tin_number": None}  # You can adjust if TIN is in sheet
        )

        # Iterate rows
        for _, row in data.iterrows():
            try:
                invoice_date = pd.to_datetime(row.get("INVOINCE DATE"), errors="coerce")
                payment_date = pd.to_datetime(row.get("PAYMENT DATE"), errors="coerce")

                FacilityRecord.objects.create(
                    district=district,
                    facility_name=row.get("FACILITY"),
                    invoice_number=str(row.get("INVOICE NUMBER")),
                    invoice_date=invoice_date if not pd.isna(invoice_date) else None,
                    invoice_amount=row.get("INVOICE AMOUNT") or 0,
                    payment_date=payment_date if not pd.isna(payment_date) else None,
                    amount_paid=row.get("AMOUNT PAID") or 0,
                    balance=row.get("BALANCE") or 0,
                )
            except Exception as e:
                print(f"Skipping row due to error: {e}")