# -*- coding: utf-8 -*-
from django.contrib import admin

from soato import models


class Regioninline(admin.TabularInline):
    model = models.Region


class DistrictInine(admin.TabularInline):
    model = models.District


class CityInline(admin.TabularInline):
    model = models.City


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [Regioninline]
    list_display = [
        "soato",
        "name",
        "name_cyr",
        "name_rus",
        "name_eng",
        "created",
        "updated",
    ]
    search_fields = ["name", "soato", "name_cyr", "name_rus", "name_eng"]


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    inlines = [DistrictInine]
    list_display = [
        "soato",
        "name",
        "name_cyr",
        "name_rus",
        "name_eng",
        "created",
        "updated",
    ]
    list_filter = [
        "country__name",
        "country__name_cyr",
        "country__name_rus",
        "country__name_eng",
    ]
    search_fields = ["name", "soato", "name_cyr", "name_rus", "name_eng"]
    autocomplete_fields = ["country"]


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    inlines = [CityInline]
    list_display = [
        "soato",
        "name",
        "name_cyr",
        "name_rus",
        "name_eng",
        "created",
        "updated",
    ]
    list_filter = [
        "region__name",
        "region__name_cyr",
        "region__name_rus",
        "region__name_eng",
    ]
    search_fields = ["soato", "name", "name_cyr", "name_rus", "name_eng"]
    autocomplete_fields = ["region"]


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        "soato",
        "name",
        "name_cyr",
        "name_rus",
        "name_eng",
        "created",
        "updated",
    ]
    search_fields = ["name", "soato", "name_cyr", "name_rus", "name_eng"]
    autocomplete_fields = ["district"]
