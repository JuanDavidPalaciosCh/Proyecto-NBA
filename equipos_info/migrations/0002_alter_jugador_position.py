# Generated by Django 4.1.3 on 2022-11-20 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='position',
            field=models.CharField(max_length=20, null=True),
        ),
    ]