# Generated by Django 4.2.5 on 2023-09-27 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_product_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 9, 27, 10, 8, 39, 252553)),
        ),
    ]
