# Generated by Django 4.1.3 on 2022-11-18 10:29

from __future__ import annotations

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("incidents", "0031_incidentcosttype_incidentcost"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="incidentcost",
            options={
                "verbose_name": "Incident cost",
                "verbose_name_plural": "Incident costs",
            },
        ),
        migrations.AlterModelOptions(
            name="incidentcosttype",
            options={
                "verbose_name": "Incident cost type",
                "verbose_name_plural": "Incident cost types",
            },
        ),
    ]