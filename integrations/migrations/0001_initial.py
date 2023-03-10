# Generated by Django 4.1.7 on 2023-02-17 02:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('altitude', models.PositiveIntegerField()),
                ('ebikes', models.PositiveIntegerField()),
                ('has_ebikes', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField()),
                ('normal_bikes', models.PositiveIntegerField()),
                ('payment', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('payment_terminal', models.BooleanField()),
                ('post_code', models.CharField(max_length=50, null=True)),
                ('renting', models.PositiveIntegerField()),
                ('returning', models.PositiveIntegerField()),
                ('slots', models.PositiveIntegerField()),
                ('uid', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=3)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('empty_slots', models.PositiveIntegerField(default=0)),
                ('free_bikes', models.PositiveIntegerField(default=0)),
                ('id', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('name', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField()),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrations.extra')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('company', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('gbfs_href', models.CharField(max_length=300)),
                ('href', models.CharField(max_length=300)),
                ('id', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrations.location')),
                ('stations', models.ManyToManyField(related_name='networks', to='integrations.station')),
            ],
        ),
    ]
