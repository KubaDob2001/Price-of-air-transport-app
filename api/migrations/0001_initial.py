# Generated by Django 4.2.7 on 2023-11-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirPlane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('air_carrier', models.TextField()),
                ('fuel_capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cruise_speed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('average_fuel_consumption', models.DecimalField(decimal_places=3, max_digits=5)),
                ('number_of_passengers', models.DecimalField(decimal_places=0, max_digits=4)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AirPort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=6)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=7)),
                ('country', models.TextField()),
                ('currency', models.TextField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
