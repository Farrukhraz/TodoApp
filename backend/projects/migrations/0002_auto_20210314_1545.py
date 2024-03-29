# Generated by Django 3.1.4 on 2021-03-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
        ('developers', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='developers',
            field=models.ManyToManyField(related_name='project_developers', to='developers.Developer'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tickets',
            field=models.ManyToManyField(related_name='project_tickets', to='todos.Ticket'),
        ),
    ]
