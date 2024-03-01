# Generated by Django 5.0.2 on 2024-02-21 20:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_clothe_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="clothe",
            name="category",
            field=models.CharField(
                choices=[("shirt", "Shirt"), ("hoodie", "Hoodie")],
                default="shirt",
                max_length=8,
            ),
        ),
        migrations.AddField(
            model_name="clothe",
            name="stockCount",
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="clothe",
            name="size",
            field=models.CharField(
                choices=[
                    ("small", "Small"),
                    ("medium", "Medium"),
                    ("large", "Large"),
                    ("extra-large", "Extra-large"),
                ],
                max_length=15,
            ),
        ),
    ]
