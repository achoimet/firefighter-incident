# Generated by Django 4.2.11 on 2024-04-30 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_apitokenproxy_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="apitokenproxy",
            options={
                "default_permissions": [],
                "permissions": [
                    ("can_edit_any", "Can reassign token to any user"),
                    ("can_add_any", "Can add token to any user"),
                    ("can_view_any", "Can view token of all users"),
                    ("can_delete_any", "Can delete token of any user"),
                    ("can_add_own", "Can add own tokens"),
                    ("can_view_own", "Can view own tokens"),
                    ("can_delete_own", "Can delete own tokens"),
                ],
                "verbose_name": "API Token",
                "verbose_name_plural": "API Tokens",
            },
        ),
    ]
