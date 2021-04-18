from django.core.management import call_command
from django.test import TestCase
from six import StringIO


class ManagementCase(TestCase):
    def test_soato_csv(self):
        out = StringIO()
        call_command("soato", "soato.csv", stdout=out)
        self.assertIn("Successfully", out.getvalue())
