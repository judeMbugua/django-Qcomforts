# Generated by Django 5.0.2 on 2024-02-28 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_alter_order_size"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="order",
            new_name="_order",
        ),
    ]
