# Generated by Django 3.2.5 on 2021-08-08 11:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_alter_teckstack_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teckstack',
            name='img',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpeg', 'png', 'svg'])]),
        ),
    ]
