# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-16 16:45
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0025_auto_20170814_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productiondata',
            name='hydro_fracturing_yield_increase',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Well Yield Increase Due to Hydro-fracturing'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='yield_estimation_method',
            field=models.ForeignKey(blank=True, db_column='yield_estimation_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.YieldEstimationMethod', verbose_name='Yield Estimation Method'),
        ),
    ]
