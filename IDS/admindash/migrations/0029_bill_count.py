# Generated by Django 2.1.5 on 2019-05-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindash', '0028_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
