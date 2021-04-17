# -*- coding: utf-8 -*-
from django.urls import include, path

from soato import urls_api, views

app_name = "soato"

urlpatterns = [
    path("country/", views.CountryListView.as_view(), name="country-list"),
    path(
        "country/<slug:slug>/", views.CountryDetailView.as_view(), name="country-detail"
    ),
    path("region/", views.RegionListView.as_view(), name="region-list"),
    path("region/<slug:slug>/", views.RegionDetailView.as_view(), name="region-detail"),
    path("district/", views.DistrictListView.as_view(), name="district-list"),
    path(
        "district/<slug:slug>/",
        views.DistrictDetailView.as_view(),
        name="district-detail",
    ),
    path("city/", views.CityListView.as_view(), name="city-list"),
    path("city/<slug:slug>/", views.CityDetailView.as_view(), name="city-detail"),
    path("api/", include(urls_api)),
]
