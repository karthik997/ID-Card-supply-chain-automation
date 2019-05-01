# Generated by Django 2.1.5 on 2019-05-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindash', '0029_bill_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='type',
            field=models.IntegerField(choices=[('Barcode Encoding', 199), ('Magnetic Stripe', 399), ('RFID Encoding', 699), ('Proximity-Card', 799)]),
        ),
    ]