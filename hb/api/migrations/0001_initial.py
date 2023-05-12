# Generated by Django 4.2 on 2023-04-22 11:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=50)),
                ("content", ckeditor.fields.RichTextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
