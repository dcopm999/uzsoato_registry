import csv
import logging
from typing import List

from django.core.management.base import BaseCommand

from soato import models

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class Command(BaseCommand):
    help = "Import soato"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)
        parser.add_argument(
            "--csv",
            action="store_true",
            # dest='delete',
            default=True,
            help="csv type file",
        )

    def handle(self, *args, **kwargs):
        self.filename = kwargs["file"]
        if kwargs["csv"]:
            self.csv()

    def csv(self):
        items = self._sorted(self._parse_csv())
        for item in items["country"]:
            models.Country.objects.update_or_create(**item)
        for item in items["region"]:
            models.Region.objects.update_or_create(**item)
        for item in items["district"]:
            try:
                models.District.objects.update_or_create(**item)
            except models.District.DoesNotExist:
                print(item)
        for item in items["city"]:
            try:
                models.City.objects.update_or_create(**item)
            except models.City.DoesNotExist:
                print(item)
            except models.District.DoesNotExist:
                print(item)

    def _parse_csv(self):
        result = []
        with open(self.filename) as f:
            csv_file = csv.reader(f)
            for item in csv_file:
                result.append(item)
        return result

    def _sorted(self, source: List[str]):
        result = {"country": [], "region": [], "district": [], "city": []}
        for item in source:
            if len(item[0]) == 10:
                result["city"].append(
                    dict(
                        soato=item[0], name=item[1], name_cyr=item[3], name_rus=item[5]
                    )
                )
            elif len(item[0]) == 7:
                result["district"].append(
                    dict(
                        soato=item[0], name=item[1], name_cyr=item[3], name_rus=item[5]
                    )
                )
            elif len(item[0]) == 4:
                result["region"].append(
                    dict(
                        soato=item[0], name=item[1], name_cyr=item[3], name_rus=item[5]
                    )
                )
            elif len(item[0]) == 2:
                result["country"].append(
                    dict(
                        soato=item[0], name=item[1], name_cyr=item[3], name_rus=item[5]
                    )
                )
        return result

    def save(self):
        pass

    def _trans(self, source: List[str]):
        source[6] = self.translator.translate(source[5])
        return source
