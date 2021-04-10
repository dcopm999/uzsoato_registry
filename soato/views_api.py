from rest_framework import viewsets

from soato import models, serializers


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
