# Generated by Django 4.2.7 on 2023-11-25 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='latitude',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
    ]
