import csv
import logging
import os
import ssl
from typing import List

import openpyxl
import wget
from django.conf import settings
from django.core.management.base import BaseCommand

from soato import models

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class Command(BaseCommand):
    help = "Import soato"
    OUTPUT_DIR = os.path.join(settings.MEDIA_ROOT, "soato")
    CSV_FILE = os.path.join(OUTPUT_DIR, "soato.csv")

    def add_arguments(self, parser):
        parser.add_argument(
            "--csv",
            type=str,
            dest="csv",
            default=False,
            help="from csv file",
        )
        parser.add_argument(
            "--statuz", type=str, dest="statuz", default=False, help="from stat.uz"
        )

    def handle(self, *args, **kwargs):
        if kwargs["csv"]:
            self.CSV_FILE = kwargs["csv"]
            self.from_csv()
        elif kwargs["statuz"]:
            self.from_statuz(kwargs["statuz"])

    def from_csv(self):
        items = self._sorted(self._parse_csv())
        for item in items["country"]:
            models.Country.objects.update_or_create(**item)
        for item in items["region"]:
            models.Region.objects.update_or_create(**item)
        for item in items["district"]:
            models.District.objects.update_or_create(**item)
        for item in items["city"]:
            try:
                models.City.objects.update_or_create(**item)
            except models.District.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(
                        'City does not exist (name="%s", soato="%s"): skiped'
                        % (item.get("name"), item.get("soato"))
                    )
                )
        self.stdout.write(self.style.SUCCESS("Success"))

    def from_statuz(self, url):
        excel_file = self._download(url)
        self._csv_from_excel(excel_file)
        self.from_csv()

    def _download(self, url: str) -> str:
        ssl._create_default_https_context = ssl._create_unverified_context
        FILENAME = url.split("/")[-1]
        RESULT_FILE = os.path.join(self.OUTPUT_DIR, FILENAME)

        if not os.path.exists(self.OUTPUT_DIR):
            os.makedirs(self.OUTPUT_DIR)
            self.stdout.write(
                self.style.SUCCESS(
                    "Created output dir: %s" % os.path.abspath(self.OUTPUT_DIR)
                )
            )
        if os.path.isfile(RESULT_FILE):
            os.remove(RESULT_FILE)
            self.stdout.write(self.style.SUCCESS("Removed old file: %s" % RESULT_FILE))
        self.stdout.write(self.style.SUCCESS("Downloading file form url: %s" % url))
        wget.download(url, RESULT_FILE)
        self.stdout.write(self.style.SUCCESS("\tSuccess"))
        return RESULT_FILE

    def _csv_from_excel(self, excel_file):
        excel_file = openpyxl.load_workbook(excel_file)
        excel_sheet = excel_file.get_sheet_by_name("SOATO")
        if os.path.isfile(self.CSV_FILE):
            os.remove(self.CSV_FILE)
            self.stdout.write(
                self.style.SUCCESS("Removed old csv file: %s" % self.CSV_FILE)
            )
        with open(self.CSV_FILE, "w") as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            for row in excel_sheet.rows:
                wr.writerow([cell.value for cell in row])
        self.stdout.write(
            self.style.SUCCESS("Created new csv file: %s" % self.CSV_FILE)
        )

    def _parse_csv(self):
        result = []
        with open(self.CSV_FILE) as f:
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

    def _trans(self, source: List[str]):
        source[6] = self.translator.translate(source[5])
        return source
