# Generated by Django 4.2.5 on 2023-10-16 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jira_app", "0004_alter_jiraissue_assignee_alter_jiraissue_reporter_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jiraissue",
            name="assignee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="jira_ticket_assigned_set",
                to="jira_app.jirauser",
            ),
        ),
    ]