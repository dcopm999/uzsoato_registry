#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_soato_registry
------------

Tests for `soato_registry` models module.
"""

from django.shortcuts import reverse
from django.test import TestCase
from pytils.translit import slugify

from soato import models


class CoutryCase(TestCase):
    fixtures = ["soato/fixtures/soato.json"]

    def setUp(self):
        self.query = models.Country.objects.last()

    def test_str(self):
        self.assertEqual(self.query.name, self.query.__str__())

    def test_absolute_url(self):
        url = reverse("soato:country-detail", kwargs={"slug": self.query.slug})
        self.assertEqual(self.query.get_absolute_url(), url)

    def test_save_slug(self):
        self.query.save()
        self.assertEqual(self.query.slug, slugify(self.query.name))

    def tearDown(self):
        pass


class RegionCase(TestCase):
    fixtures = ["soato/fixtures/soato.json"]

    def setUp(self):
        self.query = models.Region.objects.last()

    def test_region_str(self):
        str_name = f"{self.query.country}, {self.query.name}"
        self.assertEqual(str_name, self.query.__str__())

    def test_region_absolute_url(self):
        url = reverse("soato:region-detail", kwargs={"slug": self.query.slug})
        self.assertEqual(self.query.get_absolute_url(), url)

    def test_save_slug(self):
        self.query.save()
        self.assertEqual(self.query.slug, slugify(self.query.name))

    def tearDown(self):
        pass


class DistrictCase(TestCase):
    fixtures = ["soato/fixtures/soato.json"]

    def setUp(self):
        self.query = models.District.objects.last()

    def test_district_str(self):
        str_name = f"{self.query.region}, {self.query.name}"
        self.assertEqual(str_name, self.query.__str__())

    def test_district_absolute_url(self):
        url = reverse("soato:district-detail", kwargs={"slug": self.query.slug})
        self.assertEqual(self.query.get_absolute_url(), url)

    def test_save_slug(self):
        self.query.save()
        self.assertEqual(self.query.slug, slugify(self.query.name))

    def tearDown(self):
        pass


class CityCase(TestCase):
    fixtures = ["soato/fixtures/soato.json"]

    def setUp(self):
        self.query = models.City.objects.last()

    def test_city_str(self):
        str_name = f"{self.query.district}, {self.query.name}"
        self.assertEqual(str_name, self.query.__str__())

    def test_district_absolute_url(self):
        url = reverse("soato:city-detail", kwargs={"slug": self.query.slug})
        self.assertEqual(self.query.get_absolute_url(), url)

    def test_save_slug(self):
        self.query.save()
        self.assertEqual(self.query.slug, slugify(self.query.name))

    def tearDown(self):
        pass
