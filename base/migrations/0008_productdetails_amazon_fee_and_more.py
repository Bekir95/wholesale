# Generated by Django 4.2.11 on 2024-04-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_productdetails_fbaprices_productdetails_fbmprices'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='amazon_fee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='pick_and_pack_fee',
            field=models.FloatField(blank=True, null=True),
        ),
    ]