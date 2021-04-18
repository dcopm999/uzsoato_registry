import logging

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from soato import models

logger = logging.getLogger(__name__)


class CountryCase(TestCase):
    fixtures = ["soato/fixtures/soato.json"]

    def setUp(self):
        self.query = models.Country.objects.last()
        self.user = get_user_model()
        self.user = self.user.objects.create_user(
            username="test", email="test@test.com", password="top_secret"
        )
        self.client.login(username="test", password="top_secret")

    def test_list(self):
        response = self.client.get(reverse("soato:country-list"))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(
            reverse("soato:country-detail", kwargs={"slug": self.query.slug})
        )
        self.assertEqual(response.status_code, 200)


class RegionCase(TestCase):
    fixtures = ["soato/fixtures/soato.json"]

    def setUp(self):
        self.query = models.Region.objects.last()
        self.user = get_user_model()
        self.user = self.user.objects.create_user(
            username="test", email="test@test.com", password="top_secret"
        )
        self.client.login(username="test", password="top_secret")

    def test_list(self):
        response = self.client.get(reverse("soato:region-list"))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(
            reverse("soato:region-detail", kwargs={"slug": self.query.slug})
        )
        self.assertEqual(response.status_code, 200)


class DistrictCase(TestCase):
    fixtures = ["soato/fixtures/soato.json"]

    def setUp(self):
        self.query = models.District.objects.last()
        self.user = get_user_model()
        self.user = self.user.objects.create_user(
            username="test", email="test@test.com", password="top_secret"
        )
        self.client.login(username="test", password="top_secret")

    def test_list(self):
        response = self.client.get(reverse("soato:district-list"))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(
            reverse("soato:district-detail", kwargs={"slug": self.query.slug})
        )
        self.assertEqual(response.status_code, 200)


class CityCase(TestCase):
    fixtures = ["soato/fixtures/soato.json"]

    def setUp(self):
        self.query = models.City.objects.last()
        self.user = get_user_model()
        self.user = self.user.objects.create_user(
            username="test", email="test@test.com", password="top_secret"
        )
        self.client.login(username="test", password="top_secret")

    def test_list(self):
        response = self.client.get(reverse("soato:city-list"))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(
            reverse("soato:city-detail", kwargs={"slug": self.query.slug})
        )
        self.assertEqual(response.status_code, 200)
