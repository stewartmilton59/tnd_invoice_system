from django.urls import path
from . import views

urlpatterns = [
    path("", views.district_list, name="district_list"),
    path("district/<int:district_id>/", views.district_detail, name="district_detail"),
]