from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from soato import models

decorators = [login_required, cache_page(60)]


@method_decorator(decorators, name="dispatch")
class CountryListView(generic.ListView):
    model = models.Country


@method_decorator(decorators, name="dispatch")
class CountryDetailView(generic.DetailView):
    model = models.Country


@method_decorator(decorators, name="dispatch")
class RegionListView(generic.ListView):
    model = models.Region


@method_decorator(decorators, name="dispatch")
class RegionDetailView(generic.DetailView):
    model = models.Region


@method_decorator(decorators, name="dispatch")
class DistrictListView(generic.ListView):
    model = models.District


@method_decorator(decorators, name="dispatch")
class DistrictDetailView(generic.DetailView):
    model = models.District


@method_decorator(decorators, name="dispatch")
class CityListView(generic.ListView):
    model = models.City


@method_decorator(decorators, name="dispatch")
class CityDetailView(generic.DetailView):
    model = models.City
