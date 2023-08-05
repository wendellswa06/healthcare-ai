# Generated by Django 4.1.7 on 2023-02-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("text", models.TextField()),
                ("response", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
