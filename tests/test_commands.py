import os

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase
from six import StringIO

csv_file = os.path.join(settings.MEDIA_ROOT, "soato", "soato.csv")


class ManagementCase(TestCase):
    def test_soato(self):
        out = StringIO()
        call_command(
            "soato",
            "--statuz",
            "https://stat.uz/uploads/docs/soato(mhobt)_2020.xlsx",
            stdout=out,
        )
        self.assertIn("Success", out.getvalue())
        call_command("soato", "--csv", csv_file, stdout=out)
        self.assertIn("Success", out.getvalue())
