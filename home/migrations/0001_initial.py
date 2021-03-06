# Generated by Django 3.0.5 on 2020-04-17 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('age', models.DecimalField(decimal_places=1, max_digits=10)),
                ('mrt_station', models.DecimalField(decimal_places=5, max_digits=10)),
                ('convenience_stores', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]
