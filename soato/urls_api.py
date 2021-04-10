from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from soato import views_api

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("country", views_api.CountryViewSet)
router.register("region", views_api.RegionViewSet)
router.register("district", views_api.DistrictViewSet)
router.register("city", views_api.CityViewSet)
urlpatterns = router.urls
