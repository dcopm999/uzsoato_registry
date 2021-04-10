from rest_framework import serializers

from soato import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = "__all__"
