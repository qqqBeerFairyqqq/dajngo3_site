# Generated by Django 3.1.7 on 2021-02-26 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210226_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Актер и режисер', 'verbose_name_plural': 'Актеры и режисеры'},
        ),
    ]