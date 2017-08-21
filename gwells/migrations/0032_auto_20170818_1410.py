# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-18 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0031_auto_20170817_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysubmission',
            name='artestian_flow',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Artesian Flow'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='artestian_pressure',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Artesian Pressure'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='bedrock_depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Depth to Bedrock'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='final_casing_stick_up',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Final Stick Up'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='static_water_level',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Static Water Level'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='well_cap_type',
            field=models.CharField(blank=True, max_length=40, verbose_name='Well Cap Type'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='well_disinfected',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Well Disinfected?'),
        ),
        migrations.AddField(
            model_name='well',
            name='artestian_flow',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Artesian Flow'),
        ),
        migrations.AddField(
            model_name='well',
            name='artestian_pressure',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Artesian Pressure'),
        ),
        migrations.AddField(
            model_name='well',
            name='bedrock_depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Depth to Bedrock'),
        ),
        migrations.AddField(
            model_name='well',
            name='final_casing_stick_up',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Final Stick Up'),
        ),
        migrations.AddField(
            model_name='well',
            name='static_water_level',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Static Water Level'),
        ),
        migrations.AddField(
            model_name='well',
            name='well_cap_type',
            field=models.CharField(blank=True, max_length=40, verbose_name='Well Cap Type'),
        ),
        migrations.AddField(
            model_name='well',
            name='well_disinfected',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Well Disinfected?'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='finished_well_depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Finished Well Depth'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='total_depth_drilled',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Total Depth Drilled'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='well_yield',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, verbose_name='Estimated Well Yield'),
        ),
        migrations.AlterField(
            model_name='well',
            name='finished_well_depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Finished Well Depth'),
        ),
        migrations.AlterField(
            model_name='well',
            name='total_depth_drilled',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Total Depth Drilled'),
        ),
        migrations.AlterField(
            model_name='well',
            name='well_yield',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, verbose_name='Estimated Well Yield'),
        ),
    ]