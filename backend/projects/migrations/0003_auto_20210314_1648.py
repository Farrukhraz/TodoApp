# Generated by Django 3.1.4 on 2021-03-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0003_auto_20210314_1648'),
        ('todos', '0002_auto_20210314_1648'),
        ('projects', '0002_auto_20210314_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='developers',
            field=models.ManyToManyField(related_name='projects', to='developers.Developer'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tickets',
            field=models.ManyToManyField(related_name='projects', to='todos.Ticket'),
        ),
    ]