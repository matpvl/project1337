# Generated by Django 5.1.2 on 2024-10-31 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TargetedContact",
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
                ("phone_number", models.CharField(max_length=15, unique=True)),
                ("reply", models.CharField(blank=True, default="", max_length=255)),
                ("status", models.CharField(default="PENDING", max_length=20)),
            ],
        ),
    ]
