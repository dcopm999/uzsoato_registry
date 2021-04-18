import requests
from celery import shared_task
from celery.utils.log import get_task_logger
from requests.exceptions import ConnectionError

from soato import models

logger = get_task_logger(__name__)


@shared_task(bind=True, ignore_results=True)
def country_update(self, url: str):
    """
    Celery task for Country update
    """
    try:
        result = requests.get(url)
    except ConnectionError as msg:
        logger.info(msg)
        self.retry()
    else:
        for item in result.json():
            obj, created = models.Country.objects.update_or_create(**item)
            if not created:
                logger.info("Country updated: %s" % obj)
            else:
                logger.info("Country created: %s" % obj)


@shared_task(bind=True, ignore_results=True)
def region_update(self, url: str):
    """
    Celery task for Region update
    """
    try:
        result = requests.get(url)
    except ConnectionError as msg:
        logger.info(msg)
        self.retry()
    else:
        for item in result.json():
            obj, created = models.Region.objects.update_or_create(**item)
            if not created:
                logger.info("Region updated: %s" % obj)
            else:
                logger.info("Region created: %s" % obj)


@shared_task(bind=True, ignore_results=True)
def district_update(self, url):
    """
    Celery task for District update
    """
    try:
        result = requests.get(url)
    except ConnectionError as msg:
        logger.info(msg)
        self.retry()
    else:
        for item in result.json():
            obj, created = models.District.objects.update_or_create(**item)
            if not created:
                logger.info("District updated: %s" % obj)
            else:
                logger.info("District created: %s" % obj)


@shared_task(bind=True, ignore_results=True)
def city_update(self, url):
    """
    Celery task for City update
    """
    try:
        result = requests.get(url)
    except ConnectionError as msg:
        logger.info(msg)
        self.retry()
    else:
        for item in result.json():
            obj, created = models.City.objects.update_or_create(**item)
            if not created:
                logger.info("City updated: %s" % obj)
            else:
                logger.info("City created: %s" % obj)
