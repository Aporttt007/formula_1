# Generated by Django 5.1.4 on 2024-12-06 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("circuits", "0001_initial"),
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Race",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("laps", models.IntegerField()),
                ("race_type", models.CharField(max_length=255)),
                (
                    "circuit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="races",
                        to="circuits.circuit",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PitStop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lap_number", models.IntegerField()),
                ("duration", models.CharField(max_length=255)),
                ("reason", models.CharField(max_length=255)),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pit_stops",
                        to="teams.driver",
                    ),
                ),
                (
                    "race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pit_stops",
                        to="races.race",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RaceResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.IntegerField()),
                ("points", models.IntegerField()),
                ("fastest_lap", models.BooleanField(default=False)),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="race_results",
                        to="teams.driver",
                    ),
                ),
                (
                    "race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="races.race",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SessionTiming",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session_type", models.CharField(max_length=255)),
                ("lap_time", models.TimeField()),
                ("position", models.IntegerField()),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="session_timings",
                        to="teams.driver",
                    ),
                ),
                (
                    "race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="session_timings",
                        to="races.race",
                    ),
                ),
            ],
        ),
    ]