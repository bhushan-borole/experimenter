# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0005_experiment_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='proposed_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='proposed_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='firefox_version',
            field=models.CharField(choices=[('55.0', '55.0'), ('56.0', '56.0'), ('57.0', '57.0'), ('58.0', '58.0'), ('59.0', '59.0'), ('60.0', '60.0'), ('61.0', '61.0'), ('62.0', '62.0'), ('63.0', '63.0'), ('64.0', '64.0')], max_length=255),
        ),
    ]