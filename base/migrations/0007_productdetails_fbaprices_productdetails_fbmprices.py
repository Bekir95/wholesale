# Generated by Django 4.2.11 on 2024-04-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_productdetails_amzprices'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='fbaPrices',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='fbmPrices',
            field=models.TextField(blank=True, null=True),
        ),
    ]
