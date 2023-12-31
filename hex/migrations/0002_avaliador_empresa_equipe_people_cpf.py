# Generated by Django 4.2.7 on 2023-11-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.DecimalField(decimal_places=0, max_digits=3)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.DecimalField(decimal_places=0, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=99)),
                ('cnpj', models.DecimalField(decimal_places=0, max_digits=14)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipe', models.CharField(max_length=99)),
                ('integrantes', models.CharField(max_length=100)),
                ('qtdi', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='cpf',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=11),
            preserve_default=False,
        ),
    ]
