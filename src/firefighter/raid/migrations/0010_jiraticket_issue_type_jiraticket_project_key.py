# Generated by Django 4.1.6 on 2023-03-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("raid", "0009_alter_jiraticket_business_impact"),
    ]

    operations = [
        migrations.AddField(
            model_name="jiraticket",
            name="issue_type",
            field=models.CharField(default="Incident", max_length=128),
        ),
        migrations.AddField(
            model_name="jiraticket",
            name="project_key",
            field=models.CharField(default="INCIDENT", max_length=128),
        ),
    ]