# Generated by Django 4.1.7 on 2023-11-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("textfield", models.CharField(max_length=1000)),
                ("time", models.DateTimeField()),
            ],
        ),
    ]