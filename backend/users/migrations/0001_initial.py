# Generated by Django 3.1.4 on 2021-03-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='First name')),
                ('last_name', models.CharField(max_length=32, verbose_name='Last name')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
            ],
        ),
    ]
