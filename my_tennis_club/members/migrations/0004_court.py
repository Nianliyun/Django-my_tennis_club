# Generated by Django 4.2.7 on 2023-12-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0003_member_age"),
    ]

    operations = [
        migrations.CreateModel(
            name="Court",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("form", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
            ],
        ),
    ]
