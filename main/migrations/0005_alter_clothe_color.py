# Generated by Django 5.0.2 on 2024-02-21 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_clothe_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clothe",
            name="color",
            field=models.CharField(
                choices=[
                    ("white", "White"),
                    ("black", "Black"),
                    ("green", "Green"),
                    ("red", "Red"),
                    ("blue", "Blue"),
                    ("yellow", "Yellow"),
                    ("orange", "Orange"),
                    ("brown", "Brown"),
                ],
                max_length=8,
            ),
        ),
    ]
