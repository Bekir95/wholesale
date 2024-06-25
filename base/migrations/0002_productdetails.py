# Generated by Django 4.1.4 on 2024-03-30 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductDetails",
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
                ("salesRank", models.IntegerField(max_length=10)),
                ("salePrice", models.IntegerField(max_length=10)),
                ("profit", models.IntegerField(max_length=10)),
                ("profit_Percentage", models.IntegerField(max_length=10)),
                ("sales_Count", models.IntegerField(max_length=10)),
                ("sellers_Count", models.IntegerField(max_length=10)),
                ("weigt", models.IntegerField(max_length=10)),
                ("dimensions", models.IntegerField(max_length=10)),
                ("variation_count", models.IntegerField(max_length=10)),
            ],
        ),
    ]
