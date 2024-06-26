# Generated by Django 4.1.4 on 2024-03-30 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_productdetails_dimensions_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductDetailsCA",
            fields=[
                (
                    "productdetails_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="base.productdetails",
                    ),
                ),
            ],
            bases=("base.productdetails",),
        ),
        migrations.CreateModel(
            name="ProductDetailsUK",
            fields=[
                (
                    "productdetails_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="base.productdetails",
                    ),
                ),
            ],
            bases=("base.productdetails",),
        ),
        migrations.CreateModel(
            name="ProductDetailsUS",
            fields=[
                (
                    "productdetails_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="base.productdetails",
                    ),
                ),
            ],
            bases=("base.productdetails",),
        ),
    ]
