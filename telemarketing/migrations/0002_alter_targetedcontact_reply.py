# Generated by Django 5.1.2 on 2024-10-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("telemarketing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="targetedcontact",
            name="reply",
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]