# Generated by Django 3.1 on 2021-04-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100, verbose_name='City name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name_cyr',
            field=models.CharField(max_length=100, verbose_name='City name cyrillic'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name_eng',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='City name english'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='name_rus',
            field=models.CharField(max_length=100, verbose_name='City name russian'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name_eng',
            field=models.CharField(blank=True, max_length=30, verbose_name='Country name english'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='District name'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name_cyr',
            field=models.CharField(max_length=100, unique=True, verbose_name='District name cyrillic'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name_eng',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='District name english'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='district',
            name='name_rus',
            field=models.CharField(max_length=100, unique=True, verbose_name='District name russian'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Region name'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_cyr',
            field=models.CharField(max_length=100, unique=True, verbose_name='Region name cyrillic'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_eng',
            field=models.CharField(blank=True, max_length=100, verbose_name='Region name english'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_rus',
            field=models.CharField(max_length=100, unique=True, verbose_name='Region name russian'),
        ),
    ]