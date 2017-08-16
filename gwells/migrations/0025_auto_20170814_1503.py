# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-14 22:03
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0024_well_screen_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionData',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('production_data_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('yield_estimation_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Yield Estimation Rate')),
                ('yield_estimation_duration', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Yield Estimation Duration')),
                ('static_level', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))], verbose_name='SWL Before Test')),
                ('drawdown', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('hydro_fracturing_performed', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Hydro-fracturing Performed?')),
                ('hydro_fracturing_yield_increase', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Increase in Well Yield Due to Hydro-fracturing')),
                ('activity_submission', models.ForeignKey(blank=True, db_column='filing_number', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ActivitySubmission')),
                ('well', models.ForeignKey(blank=True, db_column='well_tag_number', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.Well')),
            ],
            options={
                'db_table': 'gwells_production_data',
            },
        ),
        migrations.CreateModel(
            name='YieldEstimationMethod',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('yield_estimation_method_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_yield_estimation_method',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.AddField(
            model_name='productiondata',
            name='yield_estimation_method',
            field=models.ForeignKey(blank=True, db_column='yield_estimation_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.YieldEstimationMethod'),
        ),
    ]
