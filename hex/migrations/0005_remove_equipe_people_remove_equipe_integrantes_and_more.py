# Generated by Django 4.2.7 on 2023-11-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hex', '0004_remove_people_equipe_equipe_people'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='people',
        ),
        migrations.RemoveField(
            model_name='equipe',
            name='integrantes',
        ),
        migrations.AddField(
            model_name='equipe',
            name='integrantes',
            field=models.ManyToManyField(to='hex.people', verbose_name='participantes'),
        ),
    ]
