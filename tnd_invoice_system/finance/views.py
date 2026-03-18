from django.shortcuts import render, get_object_or_404
from .models import District

def district_list(request):
    districts = District.objects.all()
    return render(request, "finance/district_list.html", {"districts": districts})

def district_detail(request, district_id):
    district = get_object_or_404(District, id=district_id)
    facilities = district.facilities.all()
    return render(request, "finance/district_detail.html", {"district": district, "facilities": facilities})