from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from soato import views_api

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("country", views_api.CountryViewSet, basename="country")
router.register("region", views_api.RegionViewSet, basename="region")
router.register("district", views_api.DistrictViewSet, basename="district")
router.register("city", views_api.CityViewSet, basename="city")
urlpatterns = router.urls
