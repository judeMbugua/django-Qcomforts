# Generated by Django 5.0.2 on 2024-02-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_remove_order_date_order_created_at_order_order_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="size",
            field=models.CharField(max_length=15),
        ),
    ]
