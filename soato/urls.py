# -*- coding: utf-8 -*-
from django.urls import include, path

# from soato import views


app_name = "soato"
urlpatterns = [path("", include("soato.urls_api"))]
