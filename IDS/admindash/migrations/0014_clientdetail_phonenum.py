# Generated by Django 2.1.5 on 2019-04-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindash', '0013_remove_clientdetail_phonenum'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetail',
            name='phonenum',
            field=models.CharField(default='0000000000', max_length=15, unique=True),
        ),
    ]
