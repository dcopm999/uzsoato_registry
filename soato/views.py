from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from soato import models

decorators = [login_required, cache_page(60)]


@method_decorator(decorators, name="dispatch")
class CountryListView(generic.ListView):
    model = models.Country
    template_name = "soato/country_list.html"


@method_decorator(decorators, name="dispatch")
class CountryDetailView(generic.DetailView):
    model = models.Country
    template_name = "soato/country_detail.html"


@method_decorator(decorators, name="dispatch")
class RegionListView(generic.ListView):
    model = models.Region
    template_name = "soato/region_list.html"


@method_decorator(decorators, name="dispatch")
class RegionDetailView(generic.DetailView):
    model = models.Region
    template_name = "soato/region_detail.html"


@method_decorator(decorators, name="dispatch")
class DistrictListView(generic.ListView):
    model = models.District
    template_name = "soato/district_list.html"


@method_decorator(decorators, name="dispatch")
class DistrictDetailView(generic.DetailView):
    model = models.District
    template_name = "soato/district_detail.html"


@method_decorator(decorators, name="dispatch")
class CityListView(generic.ListView):
    model = models.City
    template_name = "soato/city_list.html"


@method_decorator(decorators, name="dispatch")
class CityDetailView(generic.DetailView):
    model = models.City
    template_name = "soato/city_detail.html"
