# Generated by Django 4.2.5 on 2023-09-27 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_product_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 9, 27, 9, 54, 25, 914973)),
        ),
    ]