# Generated by Django 3.2.5 on 2021-08-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20210731_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]