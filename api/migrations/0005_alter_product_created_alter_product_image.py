# Generated by Django 4.2.5 on 2023-09-26 21:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_created_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 9, 27, 0, 52, 14, 901153)),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]