# -*- coding: utf-8 -*-
from django.core import validators
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from pytils.translit import slugify


class Country(models.Model):
    soato = models.CharField(
        max_length=2,
        db_index=True,
        validators=[
            validators.RegexValidator(
                regex=r"^\d{2}$", message=_("SOATO number must be 2 numbers")
            )
        ],
        verbose_name=_("SOATO"),
    )
    name = models.CharField(max_length=30, unique=True, verbose_name=_("Country name"))
    name_cyr = models.CharField(
        max_length=30, unique=True, verbose_name=_("Country name cyrillic")
    )
    name_rus = models.CharField(
        max_length=30, unique=True, verbose_name=_("Country name russian")
    )
    name_eng = models.CharField(
        max_length=30, blank=True, verbose_name=_("Country name english")
    )
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def get_absolute_url(self):
        return reverse("soato:country-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Region(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name=_("Country"),
    )
    soato = models.CharField(
        max_length=4,
        db_index=True,
        validators=[
            validators.RegexValidator(
                regex=r"^\d{4}$", message=_("SOATO number must be 4 numbers")
            )
        ],
        verbose_name=_("SOATO"),
    )
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Region name"))
    name_cyr = models.CharField(
        max_length=100, unique=True, verbose_name=_("Region name cyrillic")
    )
    name_rus = models.CharField(
        max_length=100, unique=True, verbose_name=_("Region name russian")
    )
    name_eng = models.CharField(
        max_length=100, blank=True, verbose_name=_("Region name english")
    )
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def get_absolute_url(self):
        return reverse("soato:region-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.country}, {self.name}"

    def save(self, *args, **kwargs):
        self.country = Country.objects.get(soato=self.soato[0:2])
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class District(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        verbose_name=_("Region"),
    )
    soato = models.CharField(
        db_index=True,
        max_length=7,
        validators=[
            validators.RegexValidator(
                regex=r"^\d{7}", message=_("SOATO number must be 7 numbers")
            )
        ],
        verbose_name=_("SOATO"),
    )
    name = models.CharField(
        max_length=100, unique=True, verbose_name=_("District name")
    )
    name_cyr = models.CharField(
        max_length=100, unique=True, verbose_name=_("District name cyrillic")
    )
    name_rus = models.CharField(
        max_length=100, unique=True, verbose_name=_("District name russian")
    )
    name_eng = models.CharField(
        max_length=100,
        verbose_name=_("District name english"),
        blank=True,
    )
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")

    def get_absolute_url(self):
        return reverse("soato:district-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.region}, {self.name}"

    def save(self, *args, **kwargs):
        self.region = Region.objects.get(soato=self.soato[0:4])
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class City(models.Model):
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        verbose_name=_("District"),
    )
    soato = models.CharField(
        db_index=True,
        max_length=10,
        validators=[
            validators.RegexValidator(
                regex=r"^\d{10}", message=_("SOATO number must be 10 numbers")
            )
        ],
        verbose_name=_("SOATO"),
    )
    name = models.CharField(max_length=100, verbose_name=_("City name"))
    name_cyr = models.CharField(max_length=100, verbose_name=_("City name cyrillic"))
    name_rus = models.CharField(max_length=100, verbose_name=_("City name russian"))
    name_eng = models.CharField(
        max_length=30,
        verbose_name=_("City name english"),
        blank=True,
    )
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def get_absolute_url(self):
        return reverse("soato:city-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.district}, {self.name}"

    def save(self, *args, **kwargs):
        self.district = District.objects.get(soato=self.soato[0:7])
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
