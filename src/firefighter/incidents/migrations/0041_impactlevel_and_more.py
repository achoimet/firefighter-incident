# Generated by Django 4.2.2 on 2023-06-13 14:18

import uuid

import django.db.models.deletion
from django.db import migrations, models
from django.utils.text import slugify


def create_impact_types_and_levels(apps, schema_editor):
    ImpactType = apps.get_model("incidents", "ImpactType")
    ImpactLevel = apps.get_model("incidents", "ImpactLevel")

    impact_types_and_levels: list[dict[str, str | list[tuple[str, str, int]]]] = [
        {
            "name": "👥 Customers Impact",
            "help_text": "Search, login, order tracking, etc.",
            "levels": [
                ("HI", "🔼 Critical issue for many customers", 15),
                ("MD", "➡️ Some customers have issues", 10),
                ("LO", "🔽 Few customers with minor issues", 5),
                ("NO", "0️⃣ No impact on customers", 0),
            ],
        },
        {
            "name": "📦 Sellers Impact",
            "help_text": "Toolbox, ingestion, etc.",
            "levels": [
                ("HI", "🔼 Key services inaccessible for most", 15),
                ("MD", "➡️ Some sellers have significant issues", 10),
                ("LO", "🔽 Few sellers with minor issues", 5),
                ("NO", "0️⃣ No impact on sellers", 0),
            ],
        },
        {
            "name": "🧑‍💼 Employees Impact",
            "help_text": "Internal tools, Gitlab, etc.",
            "levels": [
                ("HI", "🔼 Critical internal tools down", 15),
                ("MD", "➡️ Significant issues for some employees", 10),
                ("LO", "🔽 Few employees with minor issues", 5),
                ("NO", "0️⃣ No impact on employees", 0),
            ],
        },
        {
            "name": "💰 Business Impact",
            "help_text": "Payment, order funnel, etc.",
            "levels": [
                ("HI", "🔼 Whole business or revenue at risk", 15),
                ("MD", "➡️ Significant business or revenue loss", 10),
                ("LO", "🔽 Minor impact on business or revenue", 5),
                ("NO", "0️⃣ No impact on business or revenue", 0),
            ],
        },
    ]

    for impact_type_data in impact_types_and_levels:
        # Update or create the impact type
        impact_type, _ = ImpactType.objects.update_or_create(
            value=slugify(impact_type_data["name"]).replace("-", "_"),
            defaults={
                "name": impact_type_data["name"],
                "help_text": impact_type_data["help_text"],
            },
        )
        for level, description, order in impact_type_data["levels"]:
            # Update or create the impact level
            ImpactLevel.objects.update_or_create(
                impact_type=impact_type,
                value=level,
                defaults={"name": description, "order": order},
            )


class Migration(migrations.Migration):
    dependencies = [
        ("incidents", "0040_priority_recommended_response_type"),
    ]

    operations: list[migrations.operations.base.Operation] = [
        migrations.CreateModel(
            name="ImpactLevel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Description for the impact level for this impact type.",
                        max_length=75,
                        null=True,
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        choices=[
                            ("HI", "🔼 High"),
                            ("MD", "➡️ Medium"),
                            ("LO", "🔽 Low"),
                            ("NO", "0️⃣ N/A"),
                        ],
                        default="NO",
                        max_length=2,
                    ),
                ),
                ("order", models.PositiveSmallIntegerField(default=10)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name="impact",
            name="incidents_impact_value_valid",
        ),
        migrations.RemoveField(
            model_name="impact",
            name="value",
        ),
        migrations.AddField(
            model_name="impacttype",
            name="order",
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name="impactlevel",
            name="impact_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="levels",
                to="incidents.impacttype",
            ),
        ),
        migrations.AddField(
            model_name="impact",
            name="impact_level",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="incidents.impactlevel",
            ),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name="impactlevel",
            constraint=models.UniqueConstraint(
                fields=("impact_type", "value"), name="unique_impact_level"
            ),
        ),
        migrations.AddConstraint(
            model_name="impactlevel",
            constraint=models.CheckConstraint(
                check=models.Q(("value__in", ["HI", "MD", "LO", "NO"])),
                name="incidents_impactlevel_value_valid",
            ),
        ),
        migrations.RunPython(create_impact_types_and_levels, migrations.RunPython.noop),
        # Can be removed once squashed
        migrations.RunSQL(
            sql="", reverse_sql="TRUNCATE TABLE incidents_impact CASCADE"
        ),
    ]