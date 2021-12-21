# Generated by Django 4.0 on 2021-12-21 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('model_name', models.CharField(max_length=30)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('processor', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('weight', models.FloatField()),
            ],
        ),
    ]
