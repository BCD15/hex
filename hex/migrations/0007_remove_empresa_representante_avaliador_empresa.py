# Generated by Django 4.2.7 on 2023-11-24 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hex', '0006_empresa_representante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='representante',
        ),
        migrations.AddField(
            model_name='avaliador',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hex.empresa', verbose_name='Avaliador'),
            preserve_default=False,
        ),
    ]
