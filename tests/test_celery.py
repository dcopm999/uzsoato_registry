from unittest import skip

from django.test import TestCase

from soato import tasks
from tests.celery import app


class CeleryCase(TestCase):
    def setUp(self):
        app.conf.update(CELERY_ALWAYS_EAGER=True)

    @skip("Wrong test")
    def test_country_update(self):
        result = tasks.country_update.delay(url="http://127.0.0.1:8000/api/country")
        self.assertEqual(result.state, "SUCCESS")
